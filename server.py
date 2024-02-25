import json
from flask import Flask, render_template
import subprocess
import random
import configparser

config = configparser.ConfigParser()
config.read('channels.ini')
CHANNELS={s:dict(config.items(s)) for s in config.sections()}["CHANNELS"]

print('Starting server with channels', CHANNELS)

YT_BASE_URL = 'https://www.youtube.com/watch?v='

CACHE = {}

app = Flask(__name__)

@app.route('/channels', methods=['GET'])
def get_channels():
    return json.dumps(CHANNELS)

@app.route('/channel/<channel_id>/random', methods=['GET'])
def get_random_channel(channel_id):
    if channel_id in CACHE and len(CACHE[channel_id]) > 0:
        result_lines = CACHE[channel_id]
    else:
        channel_url = CHANNELS[channel_id]
        result = subprocess.run(['yt-dlp', '--flat-playlist', '--print', 'id', channel_url], stdout=subprocess.PIPE)
        result_lines = result.stdout.decode('utf-8').split('\n')
        CACHE[channel_id] = result_lines

    random_video = result_lines[random.randint(0, len(result_lines))]
    return json.dumps({'url': YT_BASE_URL + random_video })

@app.route('/', methods=['GET'])
def get_web_app():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
