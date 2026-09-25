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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "cen_inter_company_transfer.utils.jinja_methods",
# 	"filters": "cen_inter_company_transfer.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cen_inter_company_transfer.install.before_install"
# after_install = "cen_inter_company_transfer.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cen_inter_company_transfer.uninstall.before_uninstall"
# after_uninstall = "cen_inter_company_transfer.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "cen_inter_company_transfer.utils.before_app_install"
# after_app_install = "cen_inter_company_transfer.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "cen_inter_company_transfer.utils.before_app_uninstall"
# after_app_uninstall = "cen_inter_company_transfer.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "cen_inter_company_transfer.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cen_inter_company_transfer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cen_inter_company_transfer.tasks.all"
# 	],
# 	"daily": [
# 		"cen_inter_company_transfer.tasks.daily"
# 	],
# 	"hourly": [
# 		"cen_inter_company_transfer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cen_inter_company_transfer.tasks.weekly"
# 	],
# 	"monthly": [
# 		"cen_inter_company_transfer.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "cen_inter_company_transfer.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "cen_inter_company_transfer.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cen_inter_company_transfer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cen_inter_company_transfer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["cen_inter_company_transfer.utils.before_request"]
# after_request = ["cen_inter_company_transfer.utils.after_request"]

# Job Events
# ----------
# before_job = ["cen_inter_company_transfer.utils.before_job"]
# after_job = ["cen_inter_company_transfer.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"cen_inter_company_transfer.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

