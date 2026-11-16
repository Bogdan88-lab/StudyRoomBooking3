"""Menu for the study room booking application."""
from booking import book_room, view_bookings, search_room, cancel_booking

def show_records(records):
    if not records:
        print("No bookings found.")
        return
    for b in records:
        print(f"ID {b['id']}: {b['student']} | Room {b['room']} | {b['date']} | {b['time']}")

while True:
    print("\nSTUDY ROOM BOOKING")
    print("1. Book a room")
    print("2. View all bookings")
    print("3. Search by room")
    print("4. Cancel a booking")
    print("5. Exit")
    choice = input("Choose 1-5: ").strip()

    if choice == "1":
        student = input("Student name: ")
        room = input("Room (A/B/C): ")
        day = input("Date (YYYY-MM-DD): ")
        time = input("Time (e.g. 10:00): ")
        print(book_room(student, room, day, time))
    elif choice == "2":
        show_records(view_bookings())
    elif choice == "3":
        room = input("Which room (A/B/C)? ")
        show_records(search_room(room))
    elif choice == "4":
        booking_id = input("Booking ID to cancel: ")
        print(cancel_booking(booking_id))
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 5.")