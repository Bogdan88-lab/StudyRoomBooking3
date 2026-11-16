"""Automated tests. Run this file with F5 in IDLE."""
import unittest
import tempfile
from pathlib import Path
import storage
from booking import book_room, view_bookings, search_room, cancel_booking

class BookingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.original_file = storage.FILE
        storage.FILE = Path(self.temp.name) / "test_bookings.csv"
        self.day = "2099-11-23"

    def tearDown(self):
        storage.FILE = self.original_file
        self.temp.cleanup()

    def test_valid_booking_is_saved(self):
        message = book_room("Sara", "A", self.day, "10:00")
        self.assertIn("Booking saved", message)
        self.assertEqual(len(view_bookings()), 1)

    def test_empty_name_is_rejected(self):
        message = book_room("   ", "A", self.day, "10:00")
        self.assertIn("Error", message)
        self.assertEqual(len(view_bookings()), 0)

    def test_search_by_room(self):
        book_room("Sara", "A", self.day, "10:00")
        book_room("Omar", "B", self.day, "10:00")
        self.assertEqual(len(search_room("A")), 1)

    def test_cancel_booking(self):
        book_room("Sara", "A", self.day, "10:00")
        booking_id = view_bookings()[0]["id"]
        self.assertIn("cancelled", cancel_booking(booking_id))
        self.assertEqual(len(view_bookings()), 0)

    def test_double_booking_is_rejected(self):
        book_room("Sara", "A", self.day, "10:00")
        message = book_room("Omar", "A", self.day, "10:00")
        self.assertIn("already booked", message.lower())
        self.assertEqual(len(view_bookings()), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)