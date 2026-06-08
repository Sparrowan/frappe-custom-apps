# Copyright (c) 2026, Alphius and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class Meeting(Document):
	def validate(self):
		if self.from_time and self.to_time and self.from_time > self.to_time:
			frappe.throw("Start Time cannot be after End Time")
		
		# Check for duplicate attendees
		attendee_ids = [attendee.attendee for attendee in self.attendees]
		if len(attendee_ids) != len(set(attendee_ids)):
			frappe.throw("Attendee cannot be added multiple times")
   
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)	

@frappe.whitelist()
def get_full_name(attendee):
	"""Returns full name of the user"""
	user_info = frappe.get_doc("User", attendee)
	return user_info.full_name