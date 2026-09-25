import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_child_doctype():
    if not frappe.db.exists("DocType", "Inter Company Branch Map"):
        doc = frappe.new_doc("DocType")
        doc.name = "Inter Company Branch Map"
        doc.module = "Cen Inter Company Transfer"
        doc.istable = 1
        doc.custom = 1
        doc.append("fields", {
            "fieldname": "branch",
            "fieldtype": "Link",
            "label": "Branch",
            "options": "Branch",
            "in_list_view": 1,
            "reqd": 1
        })
        doc.append("fields", {
            "fieldname": "receiving_warehouse",
            "fieldtype": "Link",
            "label": "Receiving Warehouse",
            "options": "Warehouse",
            "in_list_view": 1,
            "reqd": 1
        })
        doc.insert(ignore_permissions=True)

def create_inter_company_custom_fields():
    create_child_doctype()
    
    custom_fields = {
        "Customer": [
            {
                "fieldname": "custom_is_branch_wise_receiving",
                "label": "Is Branch-Wise Receiving",
                "fieldtype": "Check",
                "insert_after": "represents_company",
                "depends_on": "eval:doc.is_internal_customer == 1",
                "default": "0"
            },
            {
                "fieldname": "custom_default_receiving_warehouse",
                "label": "Default Receiving Warehouse",
                "fieldtype": "Link",
                "options": "Warehouse",
                "insert_after": "custom_is_branch_wise_receiving",
                "depends_on": "eval:doc.is_internal_customer == 1 && doc.custom_is_branch_wise_receiving == 0"
            },
            {
                "fieldname": "custom_receiving_branches",
                "label": "Receiving Branches",
                "fieldtype": "Table",
                "options": "Inter Company Branch Map",
                "insert_after": "custom_default_receiving_warehouse",
                "depends_on": "eval:doc.is_internal_customer == 1 && doc.custom_is_branch_wise_receiving == 1"
            }
        ],
        "Supplier": [
            {
                "fieldname": "custom_default_buying_price_list",
                "label": "Default Buying Price List",
                "fieldtype": "Link",
                "options": "Price List",
                "insert_after": "represents_company",
                "depends_on": "eval:doc.is_internal_supplier == 1"
            }
        ],
        "Sales Invoice": [
            {
                "fieldname": "custom_receiving_branch",
                "label": "Receiving Branch",
                "fieldtype": "Link",
                "options": "Branch",
                "insert_after": "customer",
                "depends_on": "eval:doc.custom_receiving_branch",
                "hidden": 1
            }
        ]
    }
    
    create_custom_fields(custom_fields)
