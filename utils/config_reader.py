#!/usr/bin/env python3
from pathlib import Path

import tomllib


class Config:
    _instance = None
    _data: dict

    def __new__(cls, config_path: str = "config.toml"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            path = Path(config_path)
            with open(path, "rb") as f:
                cls._instance._data = tomllib.load(f)

        return cls._instance

    def __getitem__(self, key: str):
        return self._data[key]

    def get(self, key: str, default=None):
        return self._data.get(key, default)
