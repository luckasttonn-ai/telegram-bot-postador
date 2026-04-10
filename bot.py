import requests
import json

TOKEN = "8765865198:AAEYyQc41t2dL4eHiPs1wYMROcwtphT8x50"
CHAT_ID = "-1003853792884"

with open("posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

post = posts[0]

mensagem = f"""
🔥 OFERTA DO DIA!

🛍 {post['produto']}

💰 De: {post['preco_antigo']}
💸 Por: {post['preco_novo']}

{post['descricao']}

⚠️ Promoção por tempo limitado!

🔗 COMPRE AQUI
{post['link']}
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

payload = {
    "chat_id": CHAT_ID,
    "caption": mensagem,
    "photo": post["imagem"]
}

requests.post(url, data=payload)
