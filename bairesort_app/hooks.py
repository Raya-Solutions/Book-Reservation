from . import __version__ as app_version
# Import your API function
from .api import get_occupied_rooms

# Define the API route in the get_api_methods function
def get_api_methods():
    return {
        "bairesort_app.api.get_occupied_rooms": {
            "GET": "bairesort_app.api.get_occupied_rooms",
        }
    }

app_name = "bairesort_app"
app_title = "Bairesort App"
app_publisher = "Raya Solutions"
app_description = "Beni Repo"
app_email = "ranz.manalo@rayasolutionsph.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bairesort_app/css/bairesort_app.css"
# app_include_js = "/assets/bairesort_app/js/bairesort_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/bairesort_app/css/bairesort_app.css"
# web_include_js = "/assets/bairesort_app/js/bairesort_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bairesort_app/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "bairesort_app.utils.jinja_methods",
#	"filters": "bairesort_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bairesort_app.install.before_install"
# after_install = "bairesort_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bairesort_app.uninstall.before_uninstall"
# after_uninstall = "bairesort_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bairesort_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"bairesort_app.tasks.all"
#	],
#	"daily": [
#		"bairesort_app.tasks.daily"
#	],
#	"hourly": [
#		"bairesort_app.tasks.hourly"
#	],
#	"weekly": [
#		"bairesort_app.tasks.weekly"
#	],
#	"monthly": [
#		"bairesort_app.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "bairesort_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "bairesort_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "bairesort_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bairesort_app.utils.before_request"]
# after_request = ["bairesort_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["bairesort_app.utils.before_job"]
# after_job = ["bairesort_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"bairesort_app.auth.validate"
# ]
