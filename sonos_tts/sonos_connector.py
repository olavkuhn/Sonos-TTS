#!/usr/bin/env python3
import asyncio
import socket
import threading
from pathlib import Path

from sonos_websocket import SonosWebsocket  # type: ignore[import-untyped]

from .config_reader import Config
from .exceptions import CannotFindSonosDevice
from .server import app
from .tts import TTSGenerator

config = Config()


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((config["SONOS"]["target_ip"], 1400))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


def run_flask_server():
    app.run(host="0.0.0.0", port=24505, debug=False)


async def custom_tts(input_text: str, vol: int = 0):

    config._check_init_of_config()

    speaker = SonosWebsocket(config["SONOS"]["target_ip"])
    volume = vol if vol != 0 else config["SONOS"]["volume"]

    tts = TTSGenerator()
    tts.generate_file(f"{input_text}", "c_tts.mp3")

    t = threading.Thread(target=run_flask_server, daemon=True)
    t.start()

    try:
        await speaker.play_clip(
            uri=f"http://{get_host_ip()}:24505/tts/c_tts.mp3", volume=volume
        )
    except Exception as err:
        raise CannotFindSonosDevice(config["SONOS"]["target_ip"]) from err
    finally:
        if hasattr(speaker, "close"):
            await speaker.close()
        elif hasattr(speaker, "session") and hasattr(speaker.session, "close"):
            await speaker.session.close()

    await asyncio.sleep(1)

    tts_path = Path("utils/static/tts/c_tts.mp3")

    try:
        tts_path.unlink(missing_ok=True)
    except PermissionError:
        print("No permission to remove TTS file")
    except OSError as err:
        print(f"Error removing TTS file: {err}")
