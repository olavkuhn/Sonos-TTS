import random
import string
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent
TTS_DIR = BASE_DIR / "static" / "tts"


class TTSGenerator:
    def __init__(self, voice: str = "en-GB-RyanNeural"):
        self.voice = voice
        TTS_DIR.mkdir(parents=True, exist_ok=True)

    def _generate_file_identifier(self, lenght: int = 8):
        """Generates a random alphanumeric string ID"""
        chars = string.ascii_lowercase + string.digits
        return "".join(random.choices(chars, k=lenght))

    def generate_file(self, text: str, filename: str):
        """
        This generates a single TTS audio mp3 file
        Returns the filename on success, None on failure
        """

        _full_path = TTS_DIR / filename
        command = [
            "edge-tts",
            "--text",
            text,
            "--write-media",
            str(_full_path),
            "--voice",
            self.voice,
        ]

        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            return filename
        except subprocess.CalledProcessError as e:
            print(f"Error generating {filename}: {e.stderr}")
            return None
