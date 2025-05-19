# coding: utf-8

import asyncio as _async

from src.interface.controllers.sender.controller import SenderController as _controller
from src.domain.core.rabbit.handler import Rabbit as _rabbit


async def _get_notification():
    [await _rabbit._publish(message) for message in await _controller._message()]


if __name__ == "__main__":
    _async.run(_get_notification())
