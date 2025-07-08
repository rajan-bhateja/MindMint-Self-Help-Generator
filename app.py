import asyncio

from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_community.vectorstores import FAISS

import faiss

import chainlit as cl

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
vector_store = FAISS.load_local("word_embeddings", embeddings, allow_dangerous_deserialization=True)

llm = GoogleGenerativeAI(model="gemini-2.5-flash", disable_streaming=False)

@cl.on_message
async def on_chat_start(message: cl.Message):
    query = message.content

    docs = vector_store.similarity_search_with_score(query, top_k=10)
    context = "\n\n".join([doc.page_content for doc, score in docs])

    prompt = f"""
        You are a supportive self-help advisor named MindMint.
        Use the following excerpts from classic self-help books to craft a clear, practical, actionable answer in points, preferably with examples.
        If a query is asked which is not relevant to self-help, simply respond by saying it's out of my domain.
        User's question: {query}
        
        Relevant Excerpts: {context}
    """

    # Send initial message
    response_msg = cl.Message(content="")
    await response_msg.send()

    # Stream tokens
    async for chunk in llm.astream(prompt):
        await response_msg.stream_token(chunk)
        await asyncio.sleep(0.02)

    # Final update
    await response_msg.update()