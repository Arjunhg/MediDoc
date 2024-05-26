from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from pymongo import MongoClient
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
from flask_caching import Cache
from store_index import vector_search_again
import os
import time

app = Flask(__name__)

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = os.environ.get('DB_NAME')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME')
INDEX_NAME = os.environ.get('INDEX_NAME')

MODEL_PATH = os.environ.get('MODEL_PATH')


embeddings = download_hugging_face_embeddings()

client = MongoClient(MONGO_URI)

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model=MODEL_PATH,
                  model_type="llama",
                  config={'max_new_tokens':512,    
                          'temperature':0.8})

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever = vector_search_again.as_retriever(),
    chain_type_kwargs={"prompt": PROMPT} 
)

@app.route("/")
def index():
    return render_template('chat.html')


# Configure the cache
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = os.getenv('REDIS_URL', 'redis://localhost:6379')

# Initialize the cache
cache = Cache(app)

@app.route("/get", methods=["GET", "POST"])
@cache.cached(timeout=60, query_string=True)
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa.run({"query": input})
    print("Response : ", result)  # Print the entire result
    
    # Check the type of result and access the response text accordingly
    if isinstance(result, dict) and "result" in result:
        response_text = result["result"]
    else:
        response_text = str(result)
    
    return response_text



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5000)