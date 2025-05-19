# coding: utf-8

import asyncio as _async
import typing as _t

from src.domain.entities.repositiries import Forecast as _forecast, User as _user
from src.domain.entities.external import RabbitMessage as _message
from src.interface.controllers.forecasts.controller import (
    ForecastContoller as _forecasts,
)
from src.interface.controllers.users.controller import UserContoller as _users
from src.domain.core.constants import MESSAGE_TEMPLATE


class SenderController:
    @classmethod
    async def __fetch_users(cls) -> _t.List[_user]:
        return await _users._get_user_ids()

    @classmethod
    def __message_format(cls, forecast: _forecast) -> _t.Tuple[str]:
        return MESSAGE_TEMPLATE.format(
            **forecast.__dict__,
            event="-".join([team["title"] for team in forecast.teams]),
        )

    @classmethod
    async def __send_message(cls) -> _t.List[_forecast]:
        update_planned_id, forecast = [
            _async.create_task(task(await _forecasts._get_planned_forecast()))
            for task in (_forecasts._mark_planned_forecast, _forecasts._get_forecasts)
        ]
        await _async.gather(update_planned_id, forecast)
        return await forecast

    @classmethod
    async def _message(cls):
        return [
            _message(
                chat_id=user.user_id, text=cls.__message_format(forecast)
            ).model_dump_json()
            for forecast in await cls.__send_message()
            for user in await cls.__fetch_users()
        ]
