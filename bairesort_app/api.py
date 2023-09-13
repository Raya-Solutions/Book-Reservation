import frappe

@frappe.whitelist()
def call_my_custom_function(docname):

    return "test"
