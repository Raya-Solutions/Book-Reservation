import frappe

@frappe.whitelist()
def get_occupied_rooms(check_in, check_out):
    # Fetch the list of occupied rooms for the specified date range
    occupied_rooms = []

    # Query the Booking Event DocType to find occupied rooms
    booking_events = frappe.get_all(
        "Booking Event",
        filters={
            "check_in": ("<", check_out),
            "check_out": (">", check_in),
        },
        fields=["room"],
    )

    for booking_event in booking_events:
        occupied_rooms.append(booking_event.room)

    return occupied_rooms
