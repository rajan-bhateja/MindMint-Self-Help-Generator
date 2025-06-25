# 🌿 MindMint — A Self-Help Chatbot Powered by RAG and Chainlit

**MindMint** is a Retrieval-Augmented Generation (RAG) chatbot designed to give advice inspired by timeless self-help books. Built using **Chainlit**, **Gemini 2.5 Flash**, **FAISS**, and **Google Embeddings**, it provides meaningful, encouraging responses grounded in classic personal development wisdom.

---

## 🚀 Features

- 📚 Uses 12 public domain self-help books as its core knowledge base
- 🔍 Retrieves relevant excerpts with FAISS vector search
- 🤖 Generates answers using Gemini 2.5 Flash (Google Generative AI)
- 💬 Real-time chat UI with Chainlit

## 📂 Folder Structure
```plaintext
|-- books/              # Contains .txt files of 12 public domain self-help books
|-- word_embeddings/    # FAISS vector store
|-- app.py              # Main chainlit chatbot script
|-- requirements.txt    # Python dependencies
|-- README.md           # Readme markdown file