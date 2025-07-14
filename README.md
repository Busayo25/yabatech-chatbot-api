# 🎓 YabatechEduBot

**YabatechEduBot** is a multilingual AI-powered chatbot built for students of **Yaba College of Technology**. It answers questions about school life, departments, course forms, directions, admission, and more — in **English and Yoruba**.

It comes with:
- 🔐 Secure login system
- 🌐 Language selector (English/Yoruba)
- 🧠 Semantic intent matching (understands new/unseen questions)
- 💬 Chat history tracking
- 📱 Mobile app support via REST API
- ⚙️ Web frontend using Streamlit

---

## 🧠 How It Works

- Uses [SentenceTransformers](https://www.sbert.net/) for semantic matching
- Automatically detects intents from questions using vector similarity
- Falls back to predefined responses if no match is found
- Stores chat history and users in a lightweight SQLite database

---

## 🗂️ Project Structure

├── app.py # Streamlit web app
├── chatbot.py # Chat logic with AI + DB
├── flask_api.py # API endpoint for mobile app
├── train.py # Builds embeddings from intents.json
├── intents.json # Multilingual intents and responses
├── chatbot.db # SQLite DB (users, FAQ, history)
├── requirements.txt # Required Python packages
├── .gitignore # Excludes /models/ from Git
└── models/ # (Generated during deployment)

yaml
Copy code

---

## 🚀 Deployment (on Render)

### Prerequisites:
- Python 3.9+
- `sentence-transformers` and `streamlit`

### Render Setup:
1. Push this repo to GitHub
2. Create a new Web Service at [render.com](https://render.com)
3. Use this Start Command:
   ```bash
   python train.py && python flask_api.py
Done! Your API will be available at:

arduino
Copy code
https://your-subdomain.onrender.com/chat
🧪 Testing the API
Send a POST request like:

json
Copy code
POST /chat
{
  "message": "Where is YABATECH?",
  "user": "student123",
  "language": "en"
}
Response:

json
Copy code
{
  "response": "YABATECH is in Yaba, Lagos."
}
📱 Mobile App (FlutterFlow)
A FlutterFlow project file is available here to build a no-code mobile chatbot app that connects directly to this API.

👨‍💻 Admin Login
Default test user for local testing:

Username: admin

Password: admin123

📃 License
This project is for educational and research purposes under an open license.

Made with ❤️ by Busayo Elijah
