import requests

TOKEN = "8765865198:AAEYyQc41t2dL4eHiPs1wYMROcwtphT8x50"
CHAT_ID = "-1003853792884"

mensagem = "🚀 TESTE DO BOT FUNCIONANDO!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

requests.post(url, data=payload)
