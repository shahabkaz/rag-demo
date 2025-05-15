# RAG Demo Project

This repository contains a demo implementation of a **Retrieval-Augmented Generation (RAG)** pipeline using Python and LangChain. The project integrates OpenAI's language models with a vector database (FAISS) to enable retrieval of relevant documents and generate context-aware answers.

## Features

- Document ingestion and embedding using OpenAI embeddings
- FAISS vector store for efficient similarity search
- Retrieval-augmented generation pipeline with LangChain
- Simple API to query documents with natural language questions
- Modular and extendable codebase for easy customization

## Prerequisites

- Python 3.8+
- OpenAI API key ([sign up here](https://platform.openai.com/account/api-keys))
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shahabkaz/rag-demo.git
   cd rag-demo
   ```

## 📋 Sample Output

After running the script, you will get:

Q: What is this document about?
A:  This document provides context about LangChain, a framework used for developing applications that utilize language models.