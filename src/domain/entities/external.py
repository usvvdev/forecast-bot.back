# coding: utf-8

from pydantic import BaseModel as _BM


class _Base(_BM):
    class Config:
        from_attributes = True


class Rabbit(_Base):
    host: str
    port: int
    login: str
    password: str


class RabbitMessage(_Base):
    chat_id: int
    text: str


class Target(_Base):
    id: int
    logo: str
    title: str
    header: str | int
    subHeader: str | int
    chance: str | int
    link: str
