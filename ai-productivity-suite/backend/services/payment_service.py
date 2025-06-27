import stripe
from utils.config import Config

def create_charge(amount, currency, description, source):
    config = Config()
    stripe.api_key = config.STRIPE_API_KEY
    return stripe.Charge.create(
        amount=amount,
        currency=currency,
        description=description,
        source=source
    )