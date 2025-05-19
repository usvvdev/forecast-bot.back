# coding: utf-8

import asyncio as _async
from json import loads
from ast import literal_eval
from aio_pika import IncomingMessage
from aio_pika.exceptions import AMQPConnectionError
from aiogram.exceptions import TelegramForbiddenError

from src.domain.entities.external import RabbitMessage as _message
from src.domain.core.bot.handler import TelegramBot as _bot
from src.interface.controllers.users.controller import UserContoller as _users
from src.domain.core.rabbit.handler import Rabbit as _rabbit


class Worker:
    @classmethod
    def __convert_message(cls, message: str) -> _message:
        return _message(**literal_eval(loads(message)))

    @classmethod
    async def __callback(cls, message: IncomingMessage):
        async with message.process():
            try:
                _data = cls.__convert_message(message.body)
                await _bot._inizialize().send_message(
                    chat_id=_data.chat_id,
                    text=_data.text,
                    reply_markup=_bot._keyboard(),
                )
            except TelegramForbiddenError:
                await _users._delete_user(_data.chat_id)

    @classmethod
    async def _publish_consume(cls):
        """Publish msg, reconnecting if necessary."""
        try:
            await _rabbit._connect()
        except AMQPConnectionError:
            await _rabbit._connect()
        queue = await _rabbit._declare_queue()
        await _async.sleep(2, await queue.consume(cls.__callback))


async def _send_notification():
    await _async.sleep(float("inf"), await Worker._publish_consume())


if __name__ == "__main__":
    _async.run(_send_notification())
