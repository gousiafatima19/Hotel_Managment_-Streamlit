


from rooms import add_room, view_available_rooms
from guests import register_guest, search_guest
from bookings import book_room, view_all_bookings, view_room_history
from billing import checkout_guest, generate_bill

while True:
    print("\n" + "="*50)
    print("           HOTELIO MANAGEMENT SYSTEM")
    print("="*50)
    print("""
    1. Add Room
    2. View Available Rooms
    3. Register Guest
    4. Book Room
    5. Check-Out Guest
    6. Generate Bill
    7. View All Current Bookings
    8. Search Guest by Name
    9. View Room History
    10. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_room(
            input("Room ID: "),
            input("Room Type: "),
            int(input("Price per Night: "))
        )

    elif choice == "2":
        view_available_rooms()

    elif choice == "3":
        register_guest(
            input("Guest ID: "),
            input("Guest Name: "),
            input("Contact Number: ")
        )

    elif choice == "4":
        book_room(
            input("Guest ID: "),
            input("Room ID: "),
            input("Check-in Date (YYYY-MM-DD): "),
            int(input("Number of Nights: "))
        )

    elif choice == "5":
        checkout_guest(
            input("Guest ID: "),
            input("Checkout Date (YYYY-MM-DD): ")
        )

    elif choice == "6":
        generate_bill(input("Guest ID: "))

    elif choice == "7":
        view_all_bookings()

    elif choice == "8":
        search_guest(input("Enter Guest Name: "))

    elif choice == "9":
        view_room_history(input("Enter Room ID: "))

    elif choice == "10":
        print("Thank you for using HOTELIO!")
        break

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

