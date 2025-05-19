# coding: utf-8

import typing as _t
from requests import Response as _res, get

from src.domain.core.settings import Settings as _config
from src.domain.entities.external import Target as _target


class TargetController:
    _targets_url = _config._get_setting("TARGETS_URL")

    @classmethod
    def __fetch_targets(cls, endpoint: str) -> _res:
        return get("".join((cls._targets_url, endpoint)))

    @classmethod
    def _get_links(cls) -> _t.List:
        return [
            (_target(**target).title, _target(**target).link)
            for target in cls.__fetch_targets("/api/final")
            .json()
            .get("targets")
            .get("default")
        ]

    @classmethod
    def _get_questionnaire(cls, questionnaire_id) -> _res:
        return cls.__fetch_targets(f"/api/check_sub/?id={questionnaire_id}").json()
