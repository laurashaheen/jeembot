import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'jeembot':
        if 'jeemcount' in data['text'] || 'count' in data['text']

            msg = '{} has jeemed {} times this week, get it {}'
            send_message(msg)


    def send_message(msg):
        url  = 'https://api.groupme.com/v3/bots/post'

        data = {
                'bot_id' : os.getenv('GROUPME_BOT_ID'),
                'text'   : msg,
                }
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()