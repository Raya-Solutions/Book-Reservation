import frappe
from frappe.desk.doctype.kanban_board.kanban_board import update_order
import json

@frappe.whitelist()
def validate(self=None, method=None):
	itemslist="\n"
	for result in self.items:
    		itemslist += result.item_name+"\n"
	self.custom_list_items = itemslist
	#sales_invoice = frappe.db.sql("SELECT name, custom_kitchen_status FROM `tabSales Invoice` where custom_kitchen_status ='Scheduled'",as_dict=1)
	#scheduled = []
	#done = []
	#for result in sales_invoice:
	#	if result.custom_kitchen_status == "Scheduled":
	#		scheduled.append(result.name)
	#	elif result.custom_kitchen_status == "Done":
	#		done.append(result.name)
	#data= {"Scheduled":scheduled,"Done":done}
	#print(scheduled)
	#data_str  = json.dumps(data)
	#data_json = json.loads(data_str)
	#print(data_str)
	#frappe.msgprint("test")
	#update_order('Kitchen Status',data_str)
@frappe.whitelist()
def test():
        sales_invoice = frappe.db.sql("SELECT name, custom_kitchen_status FROM `tabSales Invoice` where custom_kitchen_status ='Scheduled'",as_dict=1)
        scheduled = []
        done = []
        for result in sales_invoice:
                if result.custom_kitchen_status in ["Scheduled","Done"]:
                        scheduled.append(result.name)
                elif result.custom_kitchen_status == "Done":
                        done.append(result.name)
        data= {"Scheduled":scheduled,"Done":done}
        print(scheduled)
        data_str  = json.dumps(data)
        #data_json = json.loads(data_str)
        print(data_str)
        frappe.msgprint("test")
        update_order('Kitchen Status',data_str)
        #frappe.publish_realtime('version-update')
