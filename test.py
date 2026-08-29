import sonos_tts

# 192.168.4.37
# sonos_tts.config.update("SONOS", "target_ip", "192.168.4.37")
sonos_tts.config.update("SONOS", "volume", 50)
sonos_tts.play("Hello workd!")
