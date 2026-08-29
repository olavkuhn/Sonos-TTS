# Sonos-TTS

A lightweight Python package and CLI tool for streaming text-to-speech directly to Sonos devices using Edge TTS.

## Features

- **CLI Support**: Play TTS messages directly from your terminal.
- **Python Library**: Seamless integration into your own Python projects.
- **Config Management**: Easily configure target IP and settings programmatically or via configuration file.

## Installation

Not available, still in production.

## Quick Start

### 1. Python Usage

```python
import sonos_tts

# Update the target IP address of your Sonos speaker
sonos_tts.config.update("SONOS", "target_ip", "192.168.4.37")

# Inspect the current configuration
sonos_tts.config.see_conf()

# Play a TTS message
sonos_tts.play("Hello, world!")
```

### 2. Command Line Interface (CLI)

After installation, use the CLI directly:

```bash
sonos-tts "Hello from the terminal"
```

## Configuration

The package manages default settings inside `config.toml`. You can view or update settings dynamically via Python as shown above.

## License

MIT License
