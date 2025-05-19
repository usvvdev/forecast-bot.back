# coding: utf-8

import ast
import typing as _t
from pydantic import field_validator as _validator
from pydantic import BaseModel as _BM
from typing_extensions import TypedDict


class _Base(_BM):
    id: int

    class Config:
        from_attributes = True


class Team(TypedDict):
    title: str
    image: str


class PlannedForecast(_Base):
    id: int
    planned_datetime: str
    is_done: int


class User(_Base):
    user_id: int


class Forecast(_Base):
    sport_type: str
    datetime: str
    teams: _t.List["Team"]
    event_ratio: float
    predicted_event: str
    bet_percent: int

    @_validator("teams", mode="before")
    def conevrt_teams(cls, value: str) -> dict:
        return ast.literal_eval(value)
