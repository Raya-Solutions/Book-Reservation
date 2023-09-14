import frappe

@frappe.whitelist()
def show_custom_popup(billing_name):
    # Display a custom pop-up message
    message = "Hello Kirk!"
    frappe.msgprint(message)

