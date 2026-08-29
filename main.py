#!/usr/bin/env python3
import asyncio

from utils.sonos_connector import custom_tts


def play(text):
    asyncio.run(custom_tts(text))


play("hello world! how are you doing today!")
