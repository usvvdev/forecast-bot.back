# coding: utf-8

import typing as _t
from aiomysql import Cursor as _cur

from src.infrastructure.orm.users.executer import UserHanlder as _handler
from src.domain.entities.repositiries import User as _user


class UserContoller:
    @classmethod
    async def _save_user(cls, data: dict) -> _cur:
        return await _handler._insert_user_data(data)

    @classmethod
    async def _delete_user(cls, data: dict) -> _cur:
        return await _handler._delete_user(data)

    @classmethod
    async def _update_user(cls, data: dict) -> _cur:
        return await _handler._update_user_status(data)

    @classmethod
    async def _get_user_ids(cls) -> _t.List[_user]:
        """Get `Users` by used condition."""
        return [_user(**user_id) for user_id in await _handler._select_user_ids()]
