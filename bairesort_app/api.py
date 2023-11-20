import frappe
import json

@frappe.whitelist()
def get_table_data(guest_name):
    try:
        doc = frappe.get_doc("Reservation", guest_name)

    except Exception as e:
        doc = None
        frappe.throw(_("DocType not Fount"))
    return doc

@frappe.whitelist()
def get_invoice_id(invoice_id,guest_name):
    try:
        doc = frappe.get_doc("Reservation", guest_name)
        doc.statement = invoice_id

        doc.save()

    except Exception as e:
        doc = None
        frappe.throw(_("DocType not Fount"))
    return doc

@frappe.whitelist()
def get_cv(cvdata):
    doc = frappe.get_doc("Cash Voucher", cvdata)
    return doc


@frappe.whitelist()

def get_reservation_list():
    try:
        doc_arr = frappe.get_list('Reservation')
    except Exception as e:
        doc_arr = None
        frappe.throw(_("DocType not Fount"))
    return doc_arr

@frappe.whitelist()

def get_item_list():
    try:
        list = frappe.get_list('Item')
    except Exception as e:
        list = None
        frappe.throw(_("DocType not Fount"))
    return list

@frappe.whitelist()
def update_customer_group(customer,status,group):
    try:
        customer_doc = frappe.get_doc('Customer', customer)
        
        if status == "Confirmed Reservation":
            customer_doc.customer_group = "Scheduled"
        else:
            customer_doc.customer_group = group
            
        customer_doc.save()
        frappe.db.commit()
        return "Customer email updated successfully."
    
    except Exception as e:
        frappe.log_error(f"Error updating customer email: {str(e)}")
        return "Failed to update customer email."
    
@frappe.whitelist()
def room_status(room_list):
    room_array = json.loads(room_list)
    try:
        for room in room_array:
            item_doc = frappe.get_doc("Item",room)
            item_doc.room_status = "Dirty"

            item_doc.save()
            frappe.db.commit()
        return room_array
    except Exception as e:
        frappe.log_error(f"Error updating Item Room Status: {str(e)}")
        return "Failed to update Item Room Status."
    
@frappe.whitelist()
def get_open_shift():
    try:
         lists = frappe.get_list('POS Opening Shift',
            filters={'status': 'Open'},
            fields=['name','status', 'pos_profile'],
        )
         return lists
    except Exception as e:
        frappe.throw(_("DocType not Fount"))