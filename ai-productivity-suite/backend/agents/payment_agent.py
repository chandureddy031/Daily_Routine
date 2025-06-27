from services.payment_service import create_charge

def handle_payment(task_details):
    return create_charge(
        amount=task_details["amount"] * 100,
        currency=task_details["currency"],
        description=task_details["description"],
        source=task_details["token"]
    )