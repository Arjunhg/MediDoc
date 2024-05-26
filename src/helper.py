from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


#Extract data from the PDF
loader = PyPDFLoader("E:\StackUp\Innovating with mongoDB Atlas\Bounty\data\Medical_book.pdf")
data = loader.load()



#Create text chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
docs = text_splitter.split_documents(data)



#download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings