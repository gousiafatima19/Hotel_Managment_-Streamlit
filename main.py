import streamlit as st

from room import add_room, view_available_rooms
from guests import register_guest, search_guest
from bookings import book_room, view_all_bookings, view_room_history
from billing import checkout_guest, generate_bill


st.title("HOTELIO MANAGEMENT SYSTEM")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Room",
        "View Available Rooms",
        "Register Guest",
        "Book Room",
        "Check-Out Guest",
        "Generate Bill",
        "View All Current Bookings",
        "Search Guest by Name",
        "View Room History"
    ]
)

# 1 ADD ROOM
if menu == "Add Room":

    st.header("Add Room")

    room_id = st.text_input("Room ID")
    room_type = st.text_input("Room Type")
    price = st.number_input("Price per Night", min_value=0)

    if st.button("Add Room"):
        add_room(room_id, room_type, price)
        st.success("Room added successfully")


# 2 VIEW AVAILABLE ROOMS
elif menu == "View Available Rooms":

    st.header("Available Rooms")
    rooms = view_available_rooms()

    if rooms:
        for r in rooms:
            st.write(r)
    else:
        st.warning("No available rooms")


# 3 REGISTER GUEST
elif menu == "Register Guest":

    st.header("Register Guest")

    guest_id = st.text_input("Guest ID")
    name = st.text_input("Guest Name")
    contact = st.text_input("Contact Number")

    if st.button("Register Guest"):
        register_guest(guest_id, name, contact)
        st.success("Guest registered successfully")


# 4 BOOK ROOM
elif menu == "Book Room":

    st.header("Book Room")

    guest_id = st.text_input("Guest ID")
    room_id = st.text_input("Room ID")
    checkin = st.text_input("Check-in Date (YYYY-MM-DD)")
    nights = st.number_input("Number of Nights", min_value=1)

    if st.button("Book Room"):
        book_room(guest_id, room_id, checkin, nights)
        st.success("Room booked successfully")


# 5 CHECKOUT
elif menu == "Check-Out Guest":

    st.header("Check-Out Guest")

    guest_id = st.text_input("Guest ID")
    checkout_date = st.text_input("Checkout Date")

    if st.button("Check Out"):
        checkout_guest(guest_id, checkout_date)
        st.success("Guest checked out successfully")


# 6 GENERATE BILL
elif menu == "Generate Bill":

    st.header("Generate Bill")

    guest_id = st.text_input("Guest ID")

    if st.button("Generate Bill"):
        bill = generate_bill(guest_id)
        st.write(bill)


# 7 VIEW BOOKINGS
elif menu == "View All Current Bookings":

    st.header("Current Bookings")

    bookings = view_all_bookings()

    if bookings:
        for b in bookings:
            st.write(b)
    else:
        st.warning("No bookings found")


# 8 SEARCH GUEST
elif menu == "Search Guest by Name":

    st.header("Search Guest")

    name = st.text_input("Guest Name")

    if st.button("Search"):
        result = search_guest(name)
        st.write(result)


# 9 ROOM HISTORY
elif menu == "View Room History":

    st.header("Room History")

    room_id = st.text_input("Room ID")

    if st.button("View History"):
        history = view_room_history(room_id)
        st.write(history)