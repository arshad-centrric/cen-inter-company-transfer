app_name = "cen_inter_company_transfer"
app_title = "Centrric Inter Company Transfer"
app_publisher = "Centrric Innovations Private Limited"
app_description = "Automates inter-company and branch-wise stock transfers and invoice generation across ERPNext companies with dynamic warehouse routing."
app_email = "support@centrric.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "cen_inter_company_transfer",
# 		"logo": "/assets/cen_inter_company_transfer/logo.png",
# 		"title": "Centrric Inter Company Transfer",
# 		"route": "/cen_inter_company_transfer",
# 		"has_permission": "cen_inter_company_transfer.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cen_inter_company_transfer/css/cen_inter_company_transfer.css"
# app_include_js = "/assets/cen_inter_company_transfer/js/cen_inter_company_transfer.js"

# include js, css files in header of web template
# web_include_css = "/assets/cen_inter_company_transfer/css/cen_inter_company_transfer.css"
# web_include_js = "/assets/cen_inter_company_transfer/js/cen_inter_company_transfer.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cen_inter_company_transfer/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "cen_inter_company_transfer/public/icons.svg"

doc_events = {
    "Sales Invoice": {
        "on_submit": [
            "cen_inter_company_transfer.api.inter_company_automation.auto_create_purchase_invoice"
        ]
    }
}

after_install = [
    "cen_inter_company_transfer.setup.setup_fields.create_inter_company_custom_fields"
]

after_migrate = [
    "cen_inter_company_transfer.setup.setup_fields.create_inter_company_custom_fields"
]

doctype_js = {
    "Customer": "public/js/customer_inter_company.js",
    "Sales Invoice": "public/js/sales_invoice.js"
}
