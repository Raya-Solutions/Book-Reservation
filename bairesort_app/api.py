import frappe

@frappe.whitelist()
def call_my_custom_function(docname):
    print("Hello World")

    return "Custom function executed successfully."
