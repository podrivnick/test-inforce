from dataclasses import dataclass

from core.apps.users.config import USER_ALREADY_EXIST_ERROR
from core.apps.users.excaptions.base import BaseExceptionUser


@dataclass(frozen=True)
class UserAlreadyExists(BaseExceptionUser):
    @property
    def message(self):
        return f"{USER_ALREADY_EXIST_ERROR}"
