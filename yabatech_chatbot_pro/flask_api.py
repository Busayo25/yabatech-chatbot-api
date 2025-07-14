from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    user = data.get("user", "MobileUser")
    lang = data.get("language", "en")
    response = get_response(user_input, user=user, language=lang)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)