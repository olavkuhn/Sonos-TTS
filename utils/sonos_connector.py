import socket
import threading
import time

import soco
import tomllib
from sonos_websocket import SonosWebsocket

from utils.server import app
from utils.tts import TTSGenerator
from utils.exceptions import CannotFindSonosDevice

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((config['SONOS']['target_ip'], 1400))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return e

def run_flask_server():
    app.run(host='0.0.0.0', port=24505, debug=False)

async def custom_tts(input_text: str, vol: int = 0):
    speaker = SonosWebsocket(config['SONOS']['target_ip'])
    volume = vol if vol != 0 else config['SONOS']['volume']

    tts = TTSGenerator()
    tts.generate_file(f"{input_text}", "t1.mp3")

    t = threading.Thread(target=run_flask_server, daemon=True)
    t.start()
    
    try:
        m = await speaker.play_clip(uri=f"http://{get_host_ip()}:24505/tts/t1.mp3", volume=volume)
        print(m)
    except Exception as e:
        raise CannotFindSonosDevice(config['SONOS']['target_ip'])
    finally:
        if hasattr(speaker, 'close'):
            await speaker.close()
        elif hasattr(speaker, 'session') and hasattr(speaker.session, 'close'):
            await speaker.session.close()

    time.sleep(1)