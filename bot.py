import requests
import json
import sys

TOKEN = "8765865198:AAEYyQc41t2dL4eHiPs1wYMROcwtphT8x50"
CHAT_ID = -1003853792884

# horário do post
post_number = int(sys.argv[1])

with open("posts.json", "r") as f:
    posts = json.load(f)

post = posts[post_number]

url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

data = {
    "chat_id": CHAT_ID,
    "photo": post["imagem"],
    "caption": post["texto"],
    "parse_mode": "HTML"
}

requests.post(url, data=data)
