CUSTOM_FIELDS = [
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
        "depends_on": "eval:doc.is_internal_customer == 1 && doc.custom_is_branch_wise_receiving == 0",
        "ignore_user_permissions": 1
    },
    {
        "fieldname": "custom_default_buying_price_list",
        "label": "Default Buying Price List",
        "fieldtype": "Link",
        "options": "Price List",
        "insert_after": "custom_default_receiving_warehouse",
        "depends_on": "eval:doc.is_internal_customer == 1 && doc.custom_is_branch_wise_receiving == 0",
        "ignore_user_permissions": 1
    },
    {
        "fieldname": "custom_receiving_branches",
        "label": "Receiving Branches",
        "fieldtype": "Table",
        "options": "Inter Company Branch Map",
        "insert_after": "custom_default_buying_price_list",
        "depends_on": "eval:doc.is_internal_customer == 1 && doc.custom_is_branch_wise_receiving == 1"
    }
]
