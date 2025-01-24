import time
import datetime
import winsound
from threading import Thread
from typing import List, Tuple

class PrimeMate:
    def __init__(self):
        self.scheduled_events: List[Tuple[datetime.datetime, str]] = []

    def add_event(self, event_time: datetime.datetime, message: str):
        """Add a new event to be scheduled."""
        self.scheduled_events.append((event_time, message))
        self.scheduled_events.sort()  # Ensure the list is sorted by time
        print(f"Event scheduled: {event_time} - {message}")

    def alert(self, message: str):
        """Triggers an alert with sound and message."""
        # Play a sound (a beep in this case)
        winsound.Beep(1000, 500)  # Frequency, Duration
        # Display the message
        print(f"ALERT: {message}")

    def event_checker(self):
        """Continuously check for events and trigger alerts."""
        while True:
            now = datetime.datetime.now()
            for event_time, message in list(self.scheduled_events):
                if now >= event_time:
                    self.alert(message)
                    self.scheduled_events.remove((event_time, message))
            time.sleep(60)  # Check every minute

    def start(self):
        """Start the event checker in a separate thread."""
        print("Starting PrimeMate event checker...")
        Thread(target=self.event_checker, daemon=True).start()

if __name__ == "__main__":
    prime_mate = PrimeMate()
    prime_mate.start()

    # Example usage:
    # Schedule a reminder 1 minute from now
    one_minute_later = datetime.datetime.now() + datetime.timedelta(minutes=1)
    prime_mate.add_event(one_minute_later, "Time for your meeting!")

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("PrimeMate stopped.")