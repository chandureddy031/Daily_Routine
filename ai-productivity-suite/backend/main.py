from fastapi import FastAPI
from agents.orchestrator import Orchestrator
from services.email_service import fetch_unread_emails
import asyncio

app = FastAPI()
orchestrator = Orchestrator()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(email_processing_loop())

async def email_processing_loop():
    while True:
        emails = fetch_unread_emails()
        for email in emails:
            orchestrator.process_email(email)
        await asyncio.sleep(900)  # Process every 15 minutes