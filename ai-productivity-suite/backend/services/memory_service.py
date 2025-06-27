from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from utils.config import Config

client = QdrantClient(url=Config().QDRANT_URL)
COLLECTION_NAME = "user_preferences"

def init_memory():
    try:
        client.get_collection(COLLECTION_NAME)
    except:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE)
        )

def store_preference(user_id, key, value):
    point = PointStruct(
        id=user_id,
        vector=[0.0]*768,  # Dummy vector
        payload={"key": key, "value": value}
    )
    client.upsert(collection_name=COLLECTION_NAME, points=[point])