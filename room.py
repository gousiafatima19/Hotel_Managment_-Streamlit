rooms = [{
    "room_id": "R001",
    "room_type": "Single",  
    "price_per_night": 100
},
{
    "room_id": "R002",
    "room_type": "Double",
    "price_per_night": 150
},
{ 
    "room_id": "R003",
    "room_type": "Suite",   
    "price_per_night": 300
},
{
    "room_id": "R004",
    "room_type": "Single",  
    "price_per_night": 100
}]

def add_room(room_id, room_type, price_per_night):
    new_room = {
        "room_id": room_id,
        "room_type": room_type,
        "price_per_night": price_per_night
    }
    rooms.append(new_room)
    print("Room added successfully!")

def view_available_rooms():
    print("\nAvailable Rooms:")
    print("-" * 30)
    for r in rooms:
        print(f"Room ID: {r['room_id']}, Type: {r['room_type']}, Price: ${r['price_per_night']}")
