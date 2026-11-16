"""Read and write room bookings in a CSV file."""
import csv
from pathlib import Path

FILE = Path(__file__).with_name("bookings.csv")
FIELDS = ["id", "student", "room", "date", "time"]

def load_bookings():
    """Return all saved bookings as a list of dictionaries."""
    if not FILE.exists():
        return []
    with FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save_bookings(bookings):
    """Replace the CSV contents with the supplied bookings."""
    with FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(bookings)

def next_id(bookings):
    """Find the next ID from the existing records."""
    return str(max((int(b["id"]) for b in bookings), default=0) + 1)