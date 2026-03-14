guests = [{
    "guest_id": "G001",
    "guest_name": "John Doe",
    "contact": "1234567890"
},
{
    "guest_id": "G002",
    "guest_name": "Jane Smith",
    "contact": "0987654321"
}]

def register_guest(guest_id, guest_name, contact):
    new_guest = {
        "guest_id": guest_id,
        "guest_name": guest_name,
        "contact": contact
    }
    guests.append(new_guest)
    print("Guest registered successfully!")

def search_guest(name):
    print("\nSearch Results:")
    print("-" * 30)
    found = False
    for guest in guests:
        if name.lower() in guest["guest_name"].lower():
            print(f"ID: {guest['guest_id']}, Name: {guest['guest_name']}, Contact: {guest['contact']}")
            found = True
    if not found:
        print("No guest found")