import json
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
import random
import sqlite3
from datetime import datetime

with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

pattern_embeddings = joblib.load("models/pattern_embeddings.pkl")
tags = joblib.load("models/tags.pkl")
model = SentenceTransformer('all-MiniLM-L6-v2')

def log_chat(user, question, response, language):
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (user, question, response, language, timestamp) VALUES (?, ?, ?, ?, ?)",
              (user, question, response, language, datetime.now()))
    conn.commit()
    conn.close()

def check_database(question):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + question + '%',))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_response(user_input, user="Guest", language="en", threshold=0.6):
    user_embedding = model.encode([user_input])[0]
    sims = np.dot(pattern_embeddings, user_embedding) / (
        np.linalg.norm(pattern_embeddings, axis=1) * np.linalg.norm(user_embedding) + 1e-10)
    best_idx = np.argmax(sims)
    best_score = sims[best_idx]
    tag_lang = tags[best_idx]
    tag, tag_lang = tag_lang.split('|')

    if best_score >= threshold and tag_lang == language:
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                response = random.choice(intent["responses"][language])
                log_chat(user, user_input, response, language)
                return response
    else:
        for intent in intents["intents"]:
            if intent["tag"] == "fallback":
                response = random.choice(intent["responses"][language])
                log_chat(user, user_input, response, language)
                return response