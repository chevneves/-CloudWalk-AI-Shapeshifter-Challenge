# 🤖 CloudWalk Chatbot
A Retrieval-Augmented Generation (RAG)-based chatbot that answers user questions about **CloudWalk**, its **products** (like InfinitePay), **mission**, and **brand values** using publicly available sources.

## 📌 Project Goal
To build a chatbot that clearly explains:
- What **CloudWalk** is
- What its **products** do (e.g., InfinitePay)
- Its **mission** and **brand values**

## 🧠 Architecture Overview
This chatbot uses a **RAG** pipeline:
1. Scrapes and indexes public information about CloudWalk.
2. Embeds the data using OpenAI’s embedding model.
3. Uses **FAISS** as a vector store.
4. Leverages **LangChain** and **OpenAI GPT-4 API** to generate responses.
5. UI built with **Gradio** for easy interaction.

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+
- OpenAI API Key
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key
```

### Run the chatbot
```bash
python app.py
```

## 🧪 Sample Conversations

### 1. General Introduction
**User:** What is CloudWalk?  
**Bot:** CloudWalk is a Brazilian fintech that builds decentralized financial technologies. One of its main products is InfinitePay.

### 2. Product Information
**User:** What is InfinitePay and how does it work?  
**Bot:** InfinitePay is CloudWalk’s payment solution offering fast and secure transactions with low fees.

### 3. Mission and Brand Values
**User:** What is CloudWalk’s mission?  
**Bot:** CloudWalk's mission is to democratize the financial system using blockchain and AI technologies.

## 📚 Sources
- https://www.cloudwalk.io
- https://www.linkedin.com/company/cloudwalk/
- https://medium.com/cloudwalk

## 🔧 Stack
- Python
- LangChain
- OpenAI GPT-4
- FAISS
- Gradio
