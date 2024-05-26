
from src.helper import data, docs, download_hugging_face_embeddings
from pymongo import MongoClient
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = os.environ.get('DB_NAME')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME')
INDEX_NAME = os.environ.get('INDEX_NAME')

client = MongoClient(MONGO_URI)


MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME] 


extracted_data = docs
text_chunks = data
embeddings = download_hugging_face_embeddings()


vector_search_again = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings
)