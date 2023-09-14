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
# Assuming you have the check_in and check_out values
check_in = "2023-09-14"  # Replace with the actual check-in date
check_out = "2023-09-16"  # Replace with the actual check-out date

# Call the get_occupied_rooms function with the parameters
occupied_rooms = get_occupied_rooms(check_in, check_out)

# The `occupied_rooms` variable now contains a list of occupied rooms for the specified date range
