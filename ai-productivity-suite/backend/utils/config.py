import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        # Email
        self.IMAP_SERVER = os.getenv("IMAP_SERVER")
        self.IMAP_USER = os.getenv("IMAP_USER")
        self.IMAP_PASSWORD = os.getenv("IMAP_PASSWORD")
        
        # Calendar
        self.CALDAV_URL = os.getenv("CALDAV_URL")
        self.CALDAV_USER = os.getenv("CALDAV_USER")
        self.CALDAV_PASSWORD = os.getenv("CALDAV_PASSWORD")
        
        # Payments
        self.STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
        
        # Appwrite
        self.APPWRITE_ENDPOINT = os.getenv("APPWRITE_ENDPOINT")
        self.APPWRITE_PROJECT_ID = os.getenv("APPWRITE_PROJECT_ID")
        self.APPWRITE_API_KEY = os.getenv("APPWRITE_API_KEY")
        
        # Qdrant
        self.QDRANT_URL = os.getenv("QDRANT_URL")
        
        # LLM
        self.LLM_MODEL = os.getenv("LLM_MODEL")