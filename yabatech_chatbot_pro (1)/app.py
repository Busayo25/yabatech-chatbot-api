import streamlit as st
from chatbot import get_response
import sqlite3

st.set_page_config(page_title="YABATECH Chatbot", page_icon="🎓")

def init_db():
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    c.execute("""CREATE TABLE IF NOT EXISTS chat_history (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user TEXT, question TEXT, response TEXT,
                 language TEXT, timestamp DATETIME)""")
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result

init_db()
st.title("🎓 YABATECH Chatbot")

if "user" not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.session_state.user = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid credentials")
    st.stop()

language = st.selectbox("Choose your language / Yan ede rẹ:", ["en", "yo"], format_func=lambda x: "English" if x=="en" else "Yoruba")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:")

if user_input:
    st.session_state.messages.append(("user", user_input))
    response = get_response(user_input, user=st.session_state.user, language=language)
    st.session_state.messages.append(("bot", response))

for role, msg in st.session_state.messages:
    label = "You" if role == "user" else "Bot"
    st.markdown(f"**{label}:** {msg}")