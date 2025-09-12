from flask import Flask, render_template, request, jsonify
from model import generate_response
from search import search_web

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    # IA responde
    response = generate_response(user_input)

    # Si no sabe, busca online
    if "no sé" in response.lower() or "no entiendo" in response.lower():
        web_result = search_web(user_input)
        response = f"No estaba seguro, pero encontré esto en la web:\n\n{web_result}"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
