from . import purchase_invoice, sales_invoice


def apply_inter_company_property_setters():
    purchase_invoice.apply()
    sales_invoice.apply()
