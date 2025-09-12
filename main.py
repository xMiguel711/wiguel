from flask import Flask, request, jsonify, render_template
from model import generate_response
from search import search_web

app = Flask(__name__)

# Guardar historial en memoria
conversation_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    # Guardamos en historial
    conversation_history.append({"role": "user", "content": user_input})

    # IA responde
    response = generate_response(conversation_history)

    # Si el modelo falla → buscar en internet
    if "no sé" in response.lower() or "no entiendo" in response.lower():
        web_info = search_web(user_input)
        response = f"No estaba seguro, pero encontré esto:\n{web_info}"

    conversation_history.append({"role": "assistant", "content": response})

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
