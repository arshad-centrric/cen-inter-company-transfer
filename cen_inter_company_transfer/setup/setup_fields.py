import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_inter_company_custom_fields():
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
