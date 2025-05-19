# coding: utf-8

import typing as _t
from json import load

from src.domain.core.constants import BASE_SETTINGS_DIR


class Settings:
    _file_path: str = BASE_SETTINGS_DIR

    @classmethod
    def _settings(cls) -> _t.Dict:
        """Loading settings file."""
        with open(cls._file_path) as file_handler:
            return load(file_handler)

    @classmethod
    def _get_setting(cls, setting: str) -> str:
        """Getting current setting from the file."""
        settings = cls._settings()
        if setting not in settings:
            raise FileNotFoundError(f"error: {setting} not found")
        return settings[setting]
