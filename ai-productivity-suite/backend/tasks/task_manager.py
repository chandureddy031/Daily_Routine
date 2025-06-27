from appwrite.client import Client
from appwrite.services.database import Database
from utils.config import Config

def create_task(task_data):
    config = Config()
    client = Client()
    client.set_endpoint(config.APPWRITE_ENDPOINT)
    client.set_project(config.APPWRITE_PROJECT_ID)
    client.set_key(config.APPWRITE_API_KEY)
    
    db = Database(client)
    return db.create_document(
        database_id="unify",
        collection_id="tasks",
        document_id="unique()",
        data=task_data
    )