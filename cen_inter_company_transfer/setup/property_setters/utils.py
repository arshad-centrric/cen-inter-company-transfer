import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def set_property(doctype, fieldname, prop, value, property_type="Check"):
    name = f"{doctype}-{fieldname}-{prop}"
    if frappe.db.exists("Property Setter", name):
        return

    make_property_setter(doctype, fieldname, prop, value, property_type)


def set_ignore_user_permissions(doctype, fieldname):
    """
    Mark a Link field as exempt from User Permission list-view filtering.
    Used for fields that hold routing/counterparty metadata rather than
    the record's own owning value, so a mismatch there shouldn't hide the
    parent document from users restricted by a permission on that field's
    target doctype.
    """
    set_property(doctype, fieldname, "ignore_user_permissions", "1")
