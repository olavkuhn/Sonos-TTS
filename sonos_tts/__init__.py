#!/usr/bin/env python3
import asyncio

from .config_reader import Config
from .sonos_connector import custom_tts

_cfg = Config()


def play(text: str) -> None:
    """Play a custom text on a Sonos device through TTS."""
    asyncio.run(custom_tts(text))


class config:
    @staticmethod
    def see_conf() -> None:
        _cfg.print_config()

    @staticmethod
    def update(section: str, key: str, value: str, save: bool = True) -> None:
        _cfg.update_conf(section, key, value, save_to_file=save)
