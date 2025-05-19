# coding: utf-8

from json import dumps
from aio_pika import (
    Connection as _connection,
    Channel as _channel,
    Message as _message,
    connect_robust,
)
from aio_pika.exceptions import AMQPConnectionError

from src.domain.core.settings import Settings as _settings
from src.domain.entities.external import Rabbit as _rabbit
from src.domain.core.constants import ROUTING_KEY


class Rabbit:
    _rabbit = _rabbit(**_settings._get_setting("RABBIT"))
    _conn: _connection = None
    _base_channel: _channel = None

    @classmethod
    async def __initialize(cls) -> _connection:
        return await connect_robust(**cls._rabbit.__dict__)

    @classmethod
    async def _connect(cls):
        """Checking or creating connection."""
        if not cls._conn or cls._conn.is_closed:
            cls._conn = await cls.__initialize()
        return cls._conn

    @classmethod
    async def _channel(cls) -> _channel:
        """Creating channel."""
        if not cls._base_channel or cls._base_channel.is_closed:
            cls._base_channel = await cls._conn.channel()
        return cls._base_channel

    @classmethod
    async def _declare_queue(cls):
        await cls._channel()
        return await cls._base_channel.declare_queue(ROUTING_KEY, durable=True)

    @classmethod
    async def __publish(cls, data: dict):
        """Declare channel, publish message."""
        await cls._declare_queue()
        await cls._base_channel.default_exchange.publish(
            _message(body=dumps(data).encode()),
            routing_key=ROUTING_KEY,
        )

    @classmethod
    async def _publish(cls, data: dict):
        """Publish message, reconnecting if necessary."""
        try:
            await cls._connect()
        except AMQPConnectionError:
            await cls._connect()
        await cls.__publish(data)

    @classmethod
    async def _close(cls):
        await cls._conn.close() if cls._conn else None
