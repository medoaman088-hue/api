import os
import json
import urllib.request
from http.server import BaseHTTPRequestHandler


BOT_TOKEN = os.environ["AAEhdjp1qWlRf0eJ79gTbLyDDCTkXWyKohY"]
FAL_KEY = os.environ["d060dc8b-22ff-45d2-896b-04f890f8f3b3:ca65cadf7738fcd19678087fbbec8500"]


def telegram(method, data):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            length = int(self.headers.get("content-length", 0))
            body = self.rfile.read(length)
            update = json.loads(body)

            message = update.get("message", {})
            chat = message.get("chat", {})
            text = message.get("text", "")

            if not chat:
                self.send_response(200)
                self.end_headers()
                return

            chat_id = chat["id"]

            if text == "/start":
                telegram("sendMessage", {
                    "chat_id": chat_id,
                    "text": "🎬 ابعتلي وصف الفيديو اللي عايزه."
                })

            else:
                telegram("sendMessage", {
                    "chat_id": chat_id,
                    "text": "⏳ وصلت فكرتك، جاري تجهيز الفيديو..."
                })

            self.send_response(200)
            self.end_headers()

        except Exception as e:
            print(e)
            self.send_response(200)
            self.end_headers()
