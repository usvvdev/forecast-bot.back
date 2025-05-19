# coding: utf-8

from aiomysql import Cursor as _cur

from src.domain.core.database.handler import TableHandler as _database
from src.domain.core.constants import (
    INSERT_USER_ID,
    SELECT_USER_IDS,
    DELETE_USER,
    UPDATE_USER_STATUS,
)


class UserHanlder:
    @classmethod
    async def _select_user_ids(cls):
        """Select `user_id` data from database table."""
        cursor = await _database._execute_database_query(
            SELECT_USER_IDS, None, True
        )  # ignore
        return await cursor.fetchall()

    @classmethod
    async def _insert_user_data(cls, data: dict) -> _cur:
        """Insert `user_id` to the database table."""
        return await _database._execute_database_query(INSERT_USER_ID, data)

    @classmethod
    async def _update_user_status(cls, data: dict) -> _cur:
        return await _database._execute_database_query(UPDATE_USER_STATUS, data)

    @classmethod
    async def _delete_user(cls, data) -> _cur:
        """Update `is_active` if `user_id` is inactive."""
        return await _database._execute_database_query(DELETE_USER, data)
