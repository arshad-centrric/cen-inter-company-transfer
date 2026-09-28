import frappe


def execute():
	field_name = "Supplier-custom_default_buying_price_list"
	if frappe.db.exists("Custom Field", field_name):
		frappe.delete_doc("Custom Field", field_name, ignore_permissions=True)
