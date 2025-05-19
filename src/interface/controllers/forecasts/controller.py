# coding: utf-8

import typing as _t
from datetime import datetime as _dt

from src.domain.entities.repositiries import (
    Forecast as _forecast,
    PlannedForecast as _planned_forecast,
)
from src.infrastructure.orm.forecasts.executer import ForecastHanlder as _handler


class ForecastContoller:
    @classmethod
    def __event_time(cls, planned_forecast: _planned_forecast) -> _dt:
        """Getting event time from `Forecast` entity."""
        return _dt.strptime(planned_forecast.get("planned_datetime"), "%H:%M %d.%m.%Y")

    @classmethod
    async def _get_planned_forecast(cls) -> _t.List[_planned_forecast]:
        """Get planned `Forecasts` by `__event_time`."""
        _current_time = _dt.now().replace(second=0, microsecond=0)
        return [
            _planned_forecast(**planned_forecast)
            for planned_forecast in await _handler._select_planned_forecasts()
            if cls.__event_time(planned_forecast) == _current_time
        ]

    @classmethod
    async def _mark_planned_forecast(
        cls, planned_forecasts: _t.List[_planned_forecast]
    ) -> _planned_forecast:
        """Update planned `Forecasts` and set new value for is_done."""
        [
            await _handler._update_planned_forecasts(planned_forecast.id)
            for planned_forecast in planned_forecasts
        ]

    @classmethod
    async def _get_forecasts(
        cls, planned_forecasts: _t.List[_planned_forecast]
    ) -> _t.List[_forecast]:
        """Get `Forecasts` by condition that have been used before."""
        return [
            _forecast(**forecast)
            for planned_forecast in planned_forecasts
            for forecast in await _handler._select_forecasts(planned_forecast.id)
        ]
