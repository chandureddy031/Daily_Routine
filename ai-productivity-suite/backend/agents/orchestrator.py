from .parser_agent import parse_email
from .booking_agent import handle_booking
from .payment_agent import handle_payment
from .research_agent import handle_research
from tasks.task_manager import create_task

class Orchestrator:
    def process_email(self, email):
        parsed = parse_email(email["body"])
        for task in parsed.get("tasks", []):
            task_data = {
                "email_subject": email["subject"],
                "status": "pending",
                "details": task
            }
            create_task(task_data)
            self.execute_task(task)
    
    def execute_task(self, task):
        task_type = task["type"]
        details = task["details"]
        
        if task_type == "booking":
            result = handle_booking(details)
        elif task_type == "payment":
            result = handle_payment(details)
        elif task_type == "research":
            result = handle_research(details)
        else:
            result = {"error": "Unknown task type"}
        
        return result