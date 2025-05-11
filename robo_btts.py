import requests
import time

BOT_TOKEN = "SEU_BOT_TOKEN"
CHAT_ID = "SEU_CHAT_ID"
API_URL = "https://api-btts-sofascore.onrender.com/sinais"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    requests.post(url, data=payload)

def obter_sinais():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []

def main():
    while True:
        sinais = obter_sinais()
        for sinal in sinais:
            msg = f"{sinal['casa']} x {sinal['fora']}\nSinal: {sinal['sinal']}"
            enviar_mensagem(msg)
        time.sleep(3600)  # envia a cada 1 hora

if __name__ == "__main__":
    main()
