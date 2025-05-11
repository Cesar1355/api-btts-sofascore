from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/sinais", methods=["GET"])
def sinais():
    dados = [
        {"casa": "Time A", "fora": "Time B", "sinal": "Ambas Marcam"},
        {"casa": "Time C", "fora": "Time D", "sinal": "Ambas Marcam"}
    ]
    return jsonify(dados)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
