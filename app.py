from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Cette fonction est appelée à chaque fois que GitHub envoie un événement
    (par exemple : une nouvelle issue créée sur ton dépôt).
    """
    data = request.json  # Les infos envoyées par GitHub, au format JSON
    event_type = request.headers.get("X-GitHub-Event", "inconnu")

    print(f"Événement reçu : {event_type}")
    print(data)

    return jsonify({"status": "reçu"}), 200


@app.route("/", methods=["GET"])
def home():
    return "Le serveur fonctionne !"


if __name__ == "__main__":
    app.run(debug=True, port=5000)