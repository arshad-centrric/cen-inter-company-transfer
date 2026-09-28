import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_inter_company_purchase_invoice
from frappe.contacts.doctype.address.address import get_default_address

def auto_create_purchase_invoice(doc, method):
    """
    Triggered on_submit of Sales Invoice.
    Automatically generates a Draft Purchase Invoice for Internal Customers.
    """
    # 1. Check if this is an Internal Customer
    is_internal = frappe.db.get_value("Customer", doc.customer, "is_internal_customer")
    if not is_internal:
        return

    try:
        # --- NEW BYPASS LOGIC ---
        # ERPNext native mapper strictly requires the source Price List to have BOTH 
        # buying and selling enabled. We temporarily bypass this to allow strict price list separation.
        price_list = doc.selling_price_list
        pl_state = frappe.db.get_value("Price List", price_list, ["buying", "selling"], as_dict=True)
        
        # Temporarily enable both if they aren't
        if not pl_state.buying or not pl_state.selling:
            frappe.db.set_value("Price List", price_list, {"buying": 1, "selling": 1})
        # -------------------------

        # 2. Generate the Draft Purchase Invoice using native ERPNext mapper
        target_doc = make_inter_company_purchase_invoice(doc.name)

        # --- REVERT BYPASS LOGIC ---
        # Instantly revert the Price List back to its original state
        if not pl_state.buying or not pl_state.selling:
            frappe.db.set_value("Price List", price_list, {"buying": pl_state.buying, "selling": pl_state.selling})
        # ---------------------------

        # 3. Correct the GST billing address / GSTIN for the receiving company.
        # get_mapped_doc() blindly copies same-named fields from the Sales Invoice,
        # including the read-only, fetch_from-derived "company_gstin" field, so it
        # carries over the *selling* company's GSTIN. The native mapper also only
        # sets "billing_address" when the customer's billing address happens to
        # also be linked to the target Company. Recompute both from the actual
        # receiving company so GST validation reflects its real registration status.
        if not target_doc.billing_address:
            target_doc.billing_address = get_default_address("Company", target_doc.company)

        target_doc.company_gstin = (
            frappe.db.get_value("Address", target_doc.billing_address, "gstin")
            if target_doc.billing_address else None
        )

        # 4. Fetch Custom Defaults and Routing Logic
        customer = frappe.get_doc("Customer", doc.customer)

        receiving_warehouse = None
        receiving_branch = None
        buying_price_list = None

        if customer.custom_is_branch_wise_receiving and doc.custom_receiving_branch:
            receiving_branch = doc.custom_receiving_branch
            # Lookup the warehouse and price list mapped to this branch
            for row in customer.custom_receiving_branches:
                if row.branch == receiving_branch:
                    receiving_warehouse = row.receiving_warehouse
                    buying_price_list = row.buying_price_list
                    break
        else:
            receiving_warehouse = customer.custom_default_receiving_warehouse
            buying_price_list = customer.custom_default_buying_price_list

        # 5. Inject Defaults to bypass validation and set destination
        if buying_price_list:
            target_doc.buying_price_list = buying_price_list

        if receiving_branch:
            target_doc.branch = receiving_branch
            
        if receiving_warehouse:
            # Map the header-level "Set Accepted Warehouse"
            target_doc.set_warehouse = receiving_warehouse

            # Map the warehouse for every item row
            for item in target_doc.get("items"):
                item.warehouse = receiving_warehouse
        
        # 6. Enforce Update Stock
        target_doc.update_stock = 1

        # 7. Insert into Database as Draft (docstatus = 0)
        # using ignore_permissions ensures this bypasses strict limits without corrupting the session!
        target_doc.flags.ignore_permissions = True
        target_doc.insert(ignore_permissions=True)

        # 8. UI Feedback
        frappe.msgprint(
            f"Draft Purchase Invoice <a href='/app/purchase-invoice/{target_doc.name}' style='font-weight:bold;'>{target_doc.name}</a> has been automatically created for the receiving company.",
            title="Inter-Company Automation",
            indicator="green"
        )

    except Exception as e:
        # Failsafe revert just in case the mapper crashes
        if 'pl_state' in locals() and (not pl_state.buying or not pl_state.selling):
            frappe.db.set_value("Price List", price_list, {"buying": pl_state.buying, "selling": pl_state.selling})
            
        frappe.log_error(title=f"Inter-Company Automation Error ({doc.name})", message=frappe.get_traceback())
        frappe.throw(f"Failed to auto-generate Inter-Company Purchase Invoice. Please check the Error Log. <br><br> <b>Reason:</b> {str(e)}")