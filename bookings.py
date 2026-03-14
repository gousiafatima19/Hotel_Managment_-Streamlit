bookings = [{
    "guest_id": "G001",
    "room_id": "R001",
    "check_in_date": "2024-07-01",
    "nights": 3,
    "status": "active"
},
{
    "guest_id": "G002",
    "room_id": "R002",
    "check_in_date": "2024-07-02",
    "nights": 2,
    "status": "active"
}]

def book_room(guest_id, room_id, check_in_date, nights):
    # Check if room exists and is available
    for booking in bookings:
        if booking["room_id"] == room_id and booking["status"] == "active":
            print("Error: Room already booked!")
            return
    
    new_booking = {
        "guest_id": guest_id,
        "room_id": room_id,
        "check_in_date": check_in_date,
        "nights": nights,
        "status": "active"
    }
    bookings.append(new_booking)
    print("Room booked successfully!")

def view_all_bookings():
    print("\nAll Current Bookings:")
    print("-" * 30)
    for b in bookings:
        if b["status"] == "active":
            print(f"Guest: {b['guest_id']}, Room: {b['room_id']}, Check-in: {b['check_in_date']}, Nights: {b['nights']}")

def view_room_history(room_id):
    print(f"\nHistory for Room {room_id}:")
    print("-" * 30)
    found = False
    for b in bookings:
        if b["room_id"] == room_id:
            print(f"Guest: {b['guest_id']}, Check-in: {b['check_in_date']}, Nights: {b['nights']}, Status: {b['status']}")
            found = True
    if not found:
        print("No history found")