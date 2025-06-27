from services.calendar_service import create_event
import datetime

def handle_booking(task_details):
    return create_event(
        summary=task_details["title"],
        start=datetime.datetime.fromisoformat(task_details["start"]),
        end=datetime.datetime.fromisoformat(task_details["end"])
    )