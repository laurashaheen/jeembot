import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
abbycount = 0
husscount = 0
lauracount = 0

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'Abby' in data['name'] and 'jeemed' in data['text']:
        abbycount += 1

    if 'The' in data['name'] and 'jeemed' in data['text']:
        lauracount += 1

    if 'Hussain' in data['name'] and 'jeemed' in data['text']:
        husscount += 1

    if data['name'] != 'jeembot':
        if 'jeemcount' in data['text'] or 'count' in data['text']:
            if 'Abby' in data['name']:
                msg = 'Abby has jeemed {} times so far, get it {}'.format(abbycount,'Abigoon')
            elif 'The' in data['name']:
                msg = 'Laura has jeemed {} times so far, get it {}'.format(lauracount, 'Lalalala-laura')
            elif 'Hussain' in data['name']:
                msg = 'Hussain has jeemed {} times so far, get it {}'.format(husscount, 'Hussbitch')
        send_message(msg)


def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
            'bot_id' : os.getenv('GROUPME_BOT_ID'),
            'text'   : msg,
            }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()