import frappe

@frappe.whitelist()
def check_room_availability(check_in, check_out, room):
    # Check if the room is available for the selected date range
    available = is_room_available(check_in, check_out, room)

    # Update the Room Availability DocType
    update_room_availability(check_in, check_out, room, available)

    return {
        "message": "Room availability checked and updated successfully",
        "available": available,
    }

def is_room_available(check_in, check_out, room):
    # You can implement your own logic to check room availability here.
    # For simplicity, let's assume rooms are available unless there's a booking for the selected date range.

    # Get the list of booked rooms for the selected date range
    booked_rooms = frappe.get_all(
        "Booking Event",
        filters={
            "room": room,
            "check_in": (">=", check_in),
            "check_out": ("<=", check_out),
        },
        fields=["name"],
    )

    return not booked_rooms  # Room is available if no bookings found

def update_room_availability(check_in, check_out, room, available):
    # Update the Room Availability DocType based on the room's availability status
    room_availability = frappe.get_doc(
        "Room Availability",
        {"date": check_in, "room": room},
    )

    if room_availability:
        room_availability.available = available
        room_availability.save()
    else:
        # Create a new Room Availability record if it doesn't exist
        room_availability = frappe.new_doc("Room Availability")
        room_availability.date = check_in
        room_availability.room = room
        room_availability.available = available
        room_availability.insert()

@frappe.whitelist()
def create_room_availability(check_in, check_out, room):
    # Check if the room is available for the selected date range
    available = is_room_available(check_in, check_out, room)

    # Create a Room Availability record
    room_availability = frappe.new_doc("Room Availability")
    room_availability.date = check_in
    room_availability.room = room
    room_availability.available = available
    room_availability.insert()

    return {
        "message": "Room availability created successfully",
        "available": available,
    }
