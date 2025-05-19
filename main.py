# coding: utf-8

import asyncio as _async
from aiogram import Bot, Dispatcher as _disp, types as _tp
from aiogram.filters.command import CommandStart, CommandObject

from src.interface.controllers.targets.controller import TargetController as _target
from src.domain.core.bot.handler import TelegramBot as _bot
from src.interface.controllers.users.controller import UserContoller as _users
from src.domain.core.constants import START_MESSAGE_TEMPLATE


class ForecastBot:
    _telegram_bot: Bot = _bot._inizialize()
    _dp = _disp()

    @_dp.message(CommandStart(deep_link=True))
    async def start(message: _tp.Message, command: CommandObject):
        if bool(_target._get_questionnaire(command.args)):
            await _users._save_user(data=[message.from_user.id, command.args])
            await message.answer(text=START_MESSAGE_TEMPLATE)


async def main():
    bot = ForecastBot
    await bot._dp.start_polling(bot._telegram_bot)


if __name__ == "__main__":
    _async.run(main())
