import os
import json

DATA_FILE = 'hotel_data.txt'

# ---------- Utility Functions ----------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# ---------- Hotel Management Functions ----------

def book_room():
    data = load_data()
    room_no = input("Enter room number to book: ")
    for guest in data:
        if guest['room_no'] == room_no:
            print("❌ Room already booked!")
            return
    name = input("Enter guest name: ")
    phone = input("Enter phone number: ")
    days = input("Number of days to stay: ")

    guest = {
        'room_no': room_no,
        'name': name,
        'phone': phone,
        'days': days
    }
    data.append(guest)
    save_data(data)
    print("✅ Room booked successfully!")

def cancel_booking():
    data = load_data()
    room_no = input("Enter room number to cancel booking: ")
    new_data = [guest for guest in data if guest['room_no'] != room_no]
    if len(new_data) == len(data):
        print("❌ No booking found for that room.")
    else:
        save_data(new_data)
        print("✅ Booking cancelled.")

def check_availability():
    data = load_data()
    room_no = input("Enter room number to check: ")
    for guest in data:
        if guest['room_no'] == room_no:
            print("❌ Room is booked.")
            return
    print("✅ Room is available.")

def search_guest():
    data = load_data()
    name = input("Enter guest name to search: ")
    found = False
    for guest in data:
        if guest['name'].lower() == name.lower():
            print(f"✅ Found: Room {guest['room_no']}, Phone: {guest['phone']}, Days: {guest['days']}")
            found = True
    if not found:
        print("❌ Guest not found.")

def update_guest():
    data = load_data()
    room_no = input("Enter room number to update details: ")
    for guest in data:
        if guest['room_no'] == room_no:
            print(f"Current details: {guest}")
            guest['name'] = input("Enter new guest name: ")
            guest['phone'] = input("Enter new phone number: ")
            guest['days'] = input("Enter new number of days: ")
            save_data(data)
            print("✅ Guest details updated.")
            return
    print("❌ No booking found for that room.")

def view_all_guests():
    data = load_data()
    if not data:
        print("No guests found.")
        return
    print("\n--- Guest Records ---")
    for guest in data:
        print(f"Room: {guest['room_no']}, Name: {guest['name']}, Phone: {guest['phone']}, Days: {guest['days']}")
    print("----------------------")

# ---------- Main Menu ----------

def menu():
    while True:
        print("\n===== Hotel Management System =====")
        print("1. Book Room")
        print("2. Cancel Booking")
        print("3. Check Room Availability")
        print("4. Search Guest")
        print("5. Update Guest Details")
        print("6. View All Guest Records")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            book_room()
        elif choice == '2':
            cancel_booking()
        elif choice == '3':
            check_availability()
        elif choice == '4':
            search_guest()
        elif choice == '5':
            update_guest()
        elif choice == '6':
            view_all_guests()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ---------- Run Program ----------
menu()
