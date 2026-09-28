from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

from . import customer, sales_invoice


def create_inter_company_custom_fields():
    create_custom_fields({
        "Customer": customer.CUSTOM_FIELDS,
        "Sales Invoice": sales_invoice.CUSTOM_FIELDS,
    })
