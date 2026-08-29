#!/usr/bin/env python3
from pathlib import Path
from typing import Any

import tomllib

from .exceptions import ConfigNotComplete

CONFIG_PATH = Path(__file__).parent / "config.toml"


class Config:
    _instance = None
    _data: dict
    _config_path: Path

    def __new__(cls, config_path: Path | str = CONFIG_PATH):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config_path = Path(config_path)
            cls._instance.load()

        return cls._instance

    def load(self) -> None:
        with open(self._config_path, "rb") as f:
            self._data = tomllib.load(f)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def _check_init_of_config(self) -> None:
        if self._data.get("SONOS", {}).get("target_ip", "") == "":
            raise ConfigNotComplete()

    def update_conf(
        self, section: str, key: str, value: Any, save_to_file: bool = False
    ) -> None:
        if section not in self._data:
            self._data[section] = {}

        self._data[section][key] = value

        if save_to_file:
            self._save()

    def _save(self) -> None:
        lines = []
        for section, pairs in self._data.items():
            lines.append(f"[{section}]")
            for k, v in pairs.items():
                if isinstance(v, str):
                    lines.append(f'{k} = "{v}"')
                elif isinstance(v, bool):
                    lines.append(f"{k} = {str(v).lower()}")
                else:
                    lines.append(f"{k} = {v}")
            lines.append("")

        with open(self._config_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    def print_config(self) -> None:
        print("=== Huidige Configuratie ===")
        for section, options in self._data.items():
            print(f"\n[{section}]")
            if isinstance(options, dict):
                for k, v in options.items():
                    print(f"  {k} = {v}")
            else:
                print(f"  {options}")
        print("\n===========================")
