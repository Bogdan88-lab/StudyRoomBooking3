"""Rules for a university study room booking system."""
from datetime import date
from storage import load_bookings, save_bookings, next_id

ROOMS = {"A", "B", "C"}

def book_room(student, room, day, time):
    student = student.strip()
    room = room.strip().upper()
    day = day.strip()
    time = time.strip()

    if not student:
        return "Error: student name cannot be empty."
    if room not in ROOMS:
        return "Error: choose Room A, B or C."
    try:
        chosen_day = date.fromisoformat(day)
    except ValueError:
        return "Error: enter a real date as YYYY-MM-DD."
    if chosen_day < date.today():
        return "Error: you cannot book a past date."
    if time not in {"09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"}:
        return "Error: choose a full-hour slot from 09:00 to 16:00."

    bookings = load_bookings()
    for existing in bookings:
        if (existing["room"] == room
                and existing["date"] == day
                and existing["time"] == time):
            return "Error: room already booked for that date and time."
    new_booking = {
        "id": next_id(bookings),
        "student": student,
        "room": room,
        "date": day,
        "time": time
    }
    bookings.append(new_booking)
    save_bookings(bookings)
    return "Booking saved. Your booking ID is " + new_booking["id"]

def view_bookings():
    return load_bookings()

def search_room(room):
    room = room.strip().upper()
    return [b for b in load_bookings() if b["room"] == room]

def cancel_booking(booking_id):
    bookings = load_bookings()
    remaining = [b for b in bookings if b["id"] != str(booking_id).strip()]
    if len(remaining) == len(bookings):
        return "No booking found with that ID."
    save_bookings(remaining)
    return "Booking cancelled."