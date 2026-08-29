#!/usr/bin/env python3
import asyncio
import sys

from .sonos_connector import custom_tts


def cli() -> None:
    if len(sys.argv) < 2:
        print("Use: soco-tts <tekst>")
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    asyncio.run(custom_tts(text))


if __name__ == "__main__":
    cli()
