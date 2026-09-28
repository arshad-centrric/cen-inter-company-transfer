from .utils import set_ignore_user_permissions, set_property


def apply():
    # ERPNext's core Sales Invoice.represents_company is already exempt from
    # User Permission filtering, since it holds the internal customer's
    # represented company (the counterparty), not the transacting company.
    # Purchase Invoice.represents_company (fetch_from: supplier.represents_company)
    # is the same kind of field but was missing that flag in core, which blocked
    # receiving-side users (restricted by a Company User Permission) from seeing
    # auto-generated inter-company Purchase Invoices. Align it with Sales Invoice.
    set_ignore_user_permissions("Purchase Invoice", "represents_company")

    set_property("Purchase Invoice", "is_internal_supplier", "in_standard_filter", "1")
