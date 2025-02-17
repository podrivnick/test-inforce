from dataclasses import dataclass

from core.apps.users.config import BASE_EXCEPTION_USERS


@dataclass(frozen=True)
class BaseExceptionUser(Exception):
    product: int = None

    @property
    def message(self):
        return BASE_EXCEPTION_USERS
