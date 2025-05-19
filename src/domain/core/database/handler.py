# coding: utf-8

from asyncio import sleep
from logging import Logger as _logger
from aiomysql import connect, DictCursor, Connection, Cursor

from src.domain.core.settings import Settings as _settings


class TableHandler:
    @classmethod
    async def __conection(cls) -> Connection:
        return await sleep(0.5, await connect(**_settings._get_setting("DATABASE")))

    @classmethod
    async def _execute_database_query(
        cls, query: str, args: str, cursor_only: bool = False
    ) -> Cursor:
        """Execution database query."""
        try:
            conn = await cls.__conection()
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(query, args)
                return cur if cursor_only else await conn.commit()
        except ConnectionError as err:
            raise _logger.error({f"{cls.__name__}": "{e}".format(e=err)})
        finally:
            conn.close()

    @classmethod
    async def _insert_table_data(cls, query: str, data: dict):
        [
            (
                _logger.info({"Execution": "{value}".format(value=value)}),
                await cls._execute_database_query(
                    query=query, args=tuple(map(str, value.values()))
                ),
            )
            for value in data
        ]
