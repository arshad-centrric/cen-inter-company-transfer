import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_inter_company_purchase_invoice

def auto_create_purchase_invoice(doc, method):
    """
    Triggered on_submit of Sales Invoice.
    Automatically generates a Draft Purchase Invoice for Internal Customers.
    """
    # 1. Check if this is an Internal Customer
    is_internal = frappe.db.get_value("Customer", doc.customer, "is_internal_customer")
    if not is_internal:
        return

    # Elevate to Administrator for blind cross-company generation
    original_user = frappe.session.user
    frappe.set_user("Administrator")

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

        # 3. Fetch Custom Defaults and Routing Logic
        customer = frappe.get_doc("Customer", doc.customer)
        buying_price_list = frappe.db.get_value("Supplier", target_doc.supplier, "custom_default_buying_price_list")
        
        receiving_warehouse = None
        receiving_branch = None

        if customer.custom_is_branch_wise_receiving and doc.custom_receiving_branch:
            receiving_branch = doc.custom_receiving_branch
            # Lookup the warehouse mapped to this branch
            for row in customer.custom_receiving_branches:
                if row.branch == receiving_branch:
                    receiving_warehouse = row.receiving_warehouse
                    break
        else:
            receiving_warehouse = customer.custom_default_receiving_warehouse

        # 4. Inject Defaults to bypass validation and set destination
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
        
        # 5. Enforce Update Stock
        target_doc.update_stock = 1

        # 6. Insert into Database as Draft (docstatus = 0)
        target_doc.flags.ignore_permissions = True
        target_doc.insert()

        # 7. UI Feedback
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

    finally:
        # Always restore original user
        frappe.set_user(original_user)