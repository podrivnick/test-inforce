from dataclasses import dataclass

from core.apps.common.config import (
    SERVICE_ERROR,
    USE_CASE_EXCEPTION_USER,
)


@dataclass(frozen=True)
class ServiceException(Exception):
    product: int = None

    @property
    def message(self):
        return SERVICE_ERROR


class CustomExceptionForApps(Exception):
    status_code = 422
    default_detail = USE_CASE_EXCEPTION_USER
    default_code = "invalid"

    def __init__(self, detail=None, status_code=None, extra_data=None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = detail
        if extra_data is not None:
            self.extra_data = extra_data

    def __str__(self):
        return str(self.detail)
