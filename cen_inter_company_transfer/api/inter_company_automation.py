import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_inter_company_purchase_invoice

def auto_create_purchase_invoice(doc, method):
    """
    Triggered on_submit of Sales Invoice.
    Automatically generates a Draft Purchase Invoice for Internal Customers.
    """
    # 1. Check if this is an Internal Customer
    customer = frappe.get_doc("Customer", doc.customer)
    if not customer.is_internal_customer:
        return

    original_user = frappe.session.user
    
    try:
        # Elevate privileges to Administrator to bypass User Permissions cross-company
        frappe.set_user("Administrator")

        # --- NEW BYPASS LOGIC ---
        price_list = doc.selling_price_list
        pl_state = frappe.db.get_value("Price List", price_list, ["buying", "selling"], as_dict=True)
        
        if not pl_state.buying or not pl_state.selling:
            frappe.db.set_value("Price List", price_list, {"buying": 1, "selling": 1})
        # -------------------------

        # 2. Generate the Draft Purchase Invoice using native ERPNext mapper
        target_doc = make_inter_company_purchase_invoice(doc.name)

        # --- REVERT BYPASS LOGIC ---
        if not pl_state.buying or not pl_state.selling:
            frappe.db.set_value("Price List", price_list, {"buying": pl_state.buying, "selling": pl_state.selling})
        # ---------------------------

        # 3. Fetch Custom Defaults
        receiving_warehouse = None
        if customer.custom_is_branch_wise_receiving:
            if not doc.custom_receiving_branch:
                frappe.throw("Receiving Branch is mandatory for Branch-Wise Internal Customers.")
                
            # Find the warehouse mapped to the selected branch
            for row in customer.get("custom_receiving_branches", []):
                if row.branch == doc.custom_receiving_branch:
                    receiving_warehouse = row.receiving_warehouse
                    break
                    
            if not receiving_warehouse:
                frappe.throw(f"No receiving warehouse mapped for branch {doc.custom_receiving_branch} in Customer {doc.customer}.")
        else:
            receiving_warehouse = customer.custom_default_receiving_warehouse

        buying_price_list = frappe.db.get_value("Supplier", target_doc.supplier, "custom_default_buying_price_list")

        # 4. Inject Defaults
        if buying_price_list:
            target_doc.buying_price_list = buying_price_list
            
        if receiving_warehouse:
            target_doc.set_warehouse = receiving_warehouse
            for item in target_doc.get("items"):
                item.warehouse = receiving_warehouse
        
        # 5. Enforce Update Stock
        target_doc.update_stock = 1

        # 6. Insert into Database as Draft
        target_doc.flags.ignore_permissions = True
        target_doc.insert()

        # 7. UI Feedback
        frappe.msgprint(
            f"Draft Purchase Invoice <a href='/app/purchase-invoice/{target_doc.name}' style='font-weight:bold;'>{target_doc.name}</a> has been automatically created for the receiving company.",
            title="Inter-Company Automation",
            indicator="green"
        )

    except Exception as e:
        if 'pl_state' in locals() and (not pl_state.buying or not pl_state.selling):
            frappe.db.set_value("Price List", price_list, {"buying": pl_state.buying, "selling": pl_state.selling})
            
        frappe.log_error(title=f"Inter-Company Automation Error ({doc.name})", message=frappe.get_traceback())
        frappe.throw(f"Failed to auto-generate Inter-Company Purchase Invoice. Please check the Error Log. <br><br> <b>Reason:</b> {str(e)}")
        
    finally:
        # ALWAYS restore the original user session
        frappe.set_user(original_user)