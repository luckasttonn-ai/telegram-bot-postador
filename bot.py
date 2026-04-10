import requests
import json

TOKEN = "8765865198:AAEYyQc41t2dL4eHiPs1wYMROcwtphT8x50"
CHAT_ID = "-1003853792884"

# abrir arquivo de posts
with open("posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

# pegar primeiro post
post = posts[0]

url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

data = {
    "chat_id": CHAT_ID,
    "photo": post["imagem"],
    "caption": post["texto"]
}

res = requests.post(url, data=data)

print(res.text)
