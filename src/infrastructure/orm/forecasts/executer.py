# coding: utf-8

from aiomysql import Cursor as _cur

from src.domain.core.database.handler import TableHandler as _database
from src.domain.core.constants import (
    SELECT_FORECAST,
    SELECT_PLANNED_FORECASTS,
    UPDATE_PLANNED_FORECASTS,
)


class ForecastHanlder:
    @classmethod
    async def _update_planned_forecasts(cls, id: int) -> _cur:
        """Update `planned_forecast` data and set it into database table."""
        return await _database._execute_database_query(UPDATE_PLANNED_FORECASTS, id)

    @classmethod
    async def _select_planned_forecasts(cls) -> _cur:
        """Select `planned_forecast` data from database table."""
        cursor = await _database._execute_database_query(
            SELECT_PLANNED_FORECASTS, None, True
        )
        return await cursor.fetchall()

    @classmethod
    async def _select_forecasts(cls, id: str) -> _cur:
        """Select `forecast` data from database table."""
        cursor = await _database._execute_database_query(
            SELECT_FORECAST, id, True
        )  # ignore
        return await cursor.fetchall()
