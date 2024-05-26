# End-to-end Medical Chatbot using Llama2

![Medical Chatbot](https://example.com/your-image.png)  
## 🩺 Introduction

Welcome to the end-to-end medical chatbot project using Llama2! This project leverages the power of Meta's Llama2, LangChain, and Flask to create a highly knowledgeable and responsive medical assistant. The chatbot is designed to provide detailed answers to medical queries by integrating Mongo Atlas for vector search and Hugging Face models for inference.

## 🚀 How to Run?

### Steps to Setup and Run the Medical Chatbot

#### 1. Clone the Repository

Start by cloning the repository to your local machine and go to root folder.

```bash
cd your-repository
```

#### 2.  Create a Conda Environment

Open the repository and create a Conda environment.

```bash
conda create -n medidoc python=3.8 -y
conda activate medidoc
```

#### 3. Install the Requirements

Install all the necessary dependencies from the requirements.txt file.

```bash
pip install -r requirements.txt
```

#### 4. 🔧 Configure Environment Variables

Create a .env file in the root directory and add your Pinecone or MongoDB credentials.

```bash
MONGO_URI="your_mongo_uri"
DB_NAME="your_db_name"
COLLECTION_NAME="your_collection_name"
INDEX_NAME="your_index_name"
MODEL_PATH="your_model_path"
```

#### 5. Download and Place the Model

Download the quantized Llama2 model and place it in the model directory.

```bash
# Download the Llama 2 Model:
llama-2-7b-chat.ggmlv3.q4_0.bin

# From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

```

#### 6.▶️ Running the Project

Finally, run the application:

```bash
python app.py
```

## 🛠 Tech Stack

Python: The core programming language used for the backend logic.
LangChain: Utilized for creating the language model chain.
Flask: A lightweight WSGI web application framework for Python.
Meta Llama2: The model used for generating responses.
Mongo Atlas Vector Search: Used for storing and searching vectorized documents.
Hugging Face: Provides pre-trained models for inference.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.