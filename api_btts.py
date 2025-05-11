from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)

def buscar_sinais_btts():
    hoje = datetime.datetime.now().strftime("%Y%m%d")
    url = f"https://www.sofascore.com/football/{hoje}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, "html.parser")

    jogos = []
    for partida in soup.select(".eventRow"):
        try:
            times = partida.select_one(".cell__content").text.strip().split(" - ")
            if len(times) == 2:
                jogos.append({
                    "casa": times[0],
                    "fora": times[1],
                    "sinal": "Ambas Marcam"
                })
        except:
            continue

    return jogos

@app.route("/sinais", methods=["GET"])
def sinais():
    sinais = buscar_sinais_btts()
    return jsonify(sinais)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
