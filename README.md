# 🌿 MindMint — A Self-Help Chatbot Powered by RAG and Gemini

**MindMint** is a Retrieval-Augmented Generation (RAG) chatbot that delivers personalized, insightful self-help advice drawn from timeless public domain books. Built using FAISS, Gemini 2.5 Flash, and Chainlit, the project demonstrates the power of combining semantic search with LLM-based response generation.

---

## 🚀 Features

- 🔍 Semantic search using FAISS over 12 public domain self-help books.
- 🤖 Context-aware answer generation using Google’s Gemini 2.5 Flash model.
- 💬 Real-time chatbot interface built with Chainlit.
- 🧩 Modular and scalable RAG pipeline.

---

## 🧠 Technologies Used

| Component | Tool |
|----------|------|
| Embeddings | GoogleGenerativeAIEmbeddings (`text-embedding-004`) |
| Vector Store | FAISS |
| LLM | Gemini 2.5 Flash |
| Chat Interface | Chainlit |
| Document Loader | LangChain TextLoader |
| Chunking | RecursiveCharacterTextSplitter |

---

## 📚 Knowledge Base

MindMint retrieves context from 12 public domain self-help books, including:
- *As a Man Thinketh* by James Allen  
- *Think and Grow Rich* by Napoleon Hill  
- *The Science of Getting Rich* by Wallace D. Wattles  
- *Self-Reliance* by Ralph Waldo Emerson  
- *The Master Key System* by Charles F. Haanel
- etc...
> *(All texts are sourced from Project Gutenberg.)*

---

## 📂 Project Structure
```
├── books/              # Raw .txt files of public domain books
├── word_embeddings/    # FAISS index folder (auto-generated)
├── app.py              # Main Chainlit chatbot script
├── requirements.txt    # Project dependencies
└── README.md           # This file
```
