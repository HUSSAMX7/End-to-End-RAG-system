RAG - Retrieval-Augmented Generation System (Arabic)

This is a simple yet extendable end-to-end RAG (Retrieval-Augmented Generation) project built for Arabic documents. It demonstrates the full pipeline: from document ingestion to semantic search and language model response generation.

 **Key Features:**
- Arabic-focused document chunking & preprocessing
- LangChain-based RAG architecture
- Streamlit-based interactive interface (optional)
- Dockerized for easy deployment
- Ready to deploy on AWS EC2 + ECR


**Running Locally**

Python Virtual Environment:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

**Run with Streamlit:**

streamlit run main.py --server.port 7877


**Running with Docker:**
docker build -t capstone-rag-model .


**Run container:**

docker run -p 7877:7877 capstone-rag-model
Visit http://localhost:7877

**Deploy to AWS EC2 + ECR : **

Use the file step to move docker to ec2.txt

It contains full instructions to:

Create ECR repo

Tag & push image

**Notes:** 
This is just a starter template. The system can be extended with:

Arabic QA pipelines

Custom rerankers or retrievers

