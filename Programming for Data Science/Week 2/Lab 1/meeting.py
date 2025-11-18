from datetime import datetime

class Meeting:
    def __init__(self, name: str, time: datetime, duration: int, location: str):
        self.location = location
        self.duration = duration
        self.name = name
        self.time = time

    def get_details(self) -> None:
        print(f"{self.name} is scheduled on {self.time} at {self.location} for {self.duration} minutes.")
