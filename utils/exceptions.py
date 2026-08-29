#!/usr/bin/env python3
class CannotFindSonosDevice(Exception):
    """Exception raised when sonos_connector.py is unable to connect to Sonos device"""

    def __init__(self, ip_address: str):
        super().__init__(
            f"Unable to connect to Sonos Device with IP {ip_address}, make sure to use the same WLAN as Sonos Device"
        )
