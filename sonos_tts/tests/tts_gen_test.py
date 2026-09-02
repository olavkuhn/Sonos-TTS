import unittest
from pathlib import Path
from sonos_tts.tts import TTSGenerator, TTS_DIR

class TestTTSGenerator(unittest.TestCase):
    def test_generate_tts_file(self):
        """
        Tests if `TTSGenerator.generate_file()` generates a TTS file
        """

        _filename = "testfile.mp3"
        _desired_file_path = TTS_DIR / _filename

        ttsg = TTSGenerator()
        result = ttsg.generate_file("Hello world", _filename)

        try:
            self.assertEqual(result, _filename)
            self.assertTrue(_desired_file_path.is_file())
        finally:
            if _desired_file_path.exists():
                _desired_file_path.unlink()


if __name__ == "__main__":
    unittest.main()