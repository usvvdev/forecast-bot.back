# coding: utf-8

from aiogram import Bot as _bot
from aiogram.client.default import DefaultBotProperties as _default
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode as _parse

from src.interface.controllers.targets.controller import TargetController as _target
from src.domain.core.settings import Settings as _settings
from src.domain.core.constants import BUTTON_TEMPLATE, BUTTON_ICONS


class TelegramBot:
    _api_token: str = _settings._get_setting("BOT_TOKEN")

    @classmethod
    def _inizialize(cls):
        return _bot(
            token=cls._api_token,
            default=_default(parse_mode=_parse.HTML),
        )

    @classmethod
    def _keyboard(cls):
        buttons = [
            [
                InlineKeyboardButton(
                    text=BUTTON_TEMPLATE.format(title=title, icon=icon), url=link
                )
            ]
            for (title, link), icon in zip(_target._get_links(), BUTTON_ICONS)
        ]
        return InlineKeyboardMarkup(inline_keyboard=buttons)
