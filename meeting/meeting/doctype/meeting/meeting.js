// Copyright (c) 2026, Alphius and contributors
// For license information, please see license.txt

frappe.ui.form.on("Meeting", {
	refresh(frm) {

	},
});

frappe.ui.form.on("Meeting Attendee", {
	attendee(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		if (row.attendee) {
			frappe.call({
				method: "meeting.meeting.doctype.meeting.meeting.get_full_name",
				args: {
					attendee: row.attendee
				},
				callback: function(r) {
					if (r.message) {
						frappe.model.set_value(cdt, cdn, "full_name", r.message);
					}
				}
			});
		}
	}
});
