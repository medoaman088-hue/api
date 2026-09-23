import os
import json
import urllib.request
from http.server import BaseHTTPRequestHandler

BOT_TOKEN = os.environ["8837432914:AAEhdjp1qWlRf0eJ79gTbLyDDCTkXWyKohY"]

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{8837432914:AAEhdjp1qWlRf0eJ79gTbLyDDCTkXWyKohY}/sendMessage"

    data = json.dumps({
        "chat_id": chat_id,
        "text": text
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    urllib.request.urlopen(request)

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            length = int(self.headers.get("content-length", 0))
            body = self.rfile.read(length)
            update = json.loads(body)

            message = update.get("message", {})
            chat = message.get("chat")

            if chat:
                chat_id = chat["id"]
                text = message.get("text", "")

                if text == "/start":
                    send_message(
                        chat_id,
                        "🎬 ابعتلي وصف الفيديو اللي عايزه."
                    )
                else:
                    send_message(
                        chat_id,
                        "⏳ وصلت فكرتك، جاري تجهيز الفيديو..."
                    )

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

        except Exception as e:
            print("ERROR:", e)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
