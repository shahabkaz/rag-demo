import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA


# Load API keys
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# 1. Load Document
loader = TextLoader("documents/sample.txt")
docs = loader.load()

# 2. Split Text
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# 3. Embed & Store in FAISS
embedding_model = OpenAIEmbeddings()
db = FAISS.from_documents(split_docs, embedding_model)

# 4. Retrieval-based QA
retriever = db.as_retriever()
llm = OpenAI()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 5. Query the system
question = "What is this document about?"
response = qa_chain.invoke({"query": question})['result']
print(f"\nQ: {question}\nA: {response}")