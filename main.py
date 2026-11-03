from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Command Center Online"

def run_bot():
    os.system("python bot_handler.py")

if __name__ == "__main__":
    t = Thread(target=run_bot)
    t.start()
    app.run(host='0.0.0.0', port=8080)
