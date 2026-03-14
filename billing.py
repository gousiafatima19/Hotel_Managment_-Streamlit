from bookings import bookings

def checkout_guest(guest_id, checkout_date):
    for booking in bookings:
        if booking["guest_id"] == guest_id and booking["status"] == "active":
            if checkout_date < booking["check_in_date"]:
                print("Error: Checkout date cannot be before check-in date!")
                return
            booking["status"] = "checked_out"
            print("Guest checked out successfully!")
            return
    print("Error: No active booking found for this guest!")

def generate_bill(guest_id):
    for booking in bookings:
        if booking["guest_id"] == guest_id:
            # Find room price (simplified - in real system would get from rooms)
            price = 100  # default price
            if booking["room_id"] == "R002":
                price = 150
            elif booking["room_id"] == "R003":
                price = 300
            
            total = price * booking["nights"]
            tax = total * 0.12
            final = total + tax
            
            print("\n=== BILL SUMMARY ===")
            print(f"Guest: {guest_id}")
            print(f"Room: {booking['room_id']}")
            print(f"Stay: {booking['nights']} nights")
            print(f"Room Rate: ${price}/night")
            print(f"Total: ${total}")
            print(f"Taxes (12%): ${tax:.2f}")
            print(f"Final Amount: ${final:.2f}")
            print(f"Status: {booking['status']}")
            return
    print("Error: No booking found for this guest!")