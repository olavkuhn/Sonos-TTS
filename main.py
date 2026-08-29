#!/usr/bin/env python3
import asyncio

from utils.sonos_connector import custom_tts


def play(text):
    asyncio.run(custom_tts(text))


play("hello world! 12345, but how, if i think, how i think is cool")
