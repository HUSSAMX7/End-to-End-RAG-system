# 🧠 RAG - Retrieval-Augmented Generation System (Arabic)

This is a simple yet extendable end-to-end RAG (Retrieval-Augmented Generation) project built for Arabic documents.  
It demonstrates the full pipeline: from document ingestion to semantic search and language model response generation.

---

## ✅ Key Features

- Arabic-focused document chunking & preprocessing  
- LangChain-based RAG architecture  
- Streamlit-based interactive interface (optional)  
- Dockerized for easy deployment  
- Ready to deploy on **AWS EC2 + ECR**

---

## 🖥️ Running Locally

### 🧪 Python virtual environment:

```bash
virtualenv venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🚀 Running app using Streamlit:

```bash
streamlit run main.py --server.port 7877
```

Visit [http://localhost:7877](http://localhost:7877)

---

## 🐳 Running with Docker

### 🏗️ Build docker image locally:

```bash
docker build -t capstone-rag-model .
```

### ▶️ Run docker container:

```bash
docker run -p 7877:7877 capstone-rag-model
```

---

## ☁️ Deploy to AWS EC2 + ECR

📄 Use the file: `step to move docker to ec2.txt`  
It contains full instructions to:

- Create ECR repo  
- Tag & push docker image  
- Launch & run container on EC2 instance

---

## 📝 Notes

> This is just a **starter template** and can be extended with:

- Arabic QA pipelines  
- Custom rerankers or retrievers  
- Advanced semantic chunking  
- Vector DB integration (Qdrant, FAISS, etc.)

---

## 👨‍💻 Author Note

This project was built to demonstrate an **end-to-end AI system**, deployable on local machines or cloud environments like AWS EC2.  
It serves as a base structure for more advanced enterprise-level applications in Arabic NLP.
