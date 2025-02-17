from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass(eq=False)
class BaseQueryUserService(ABC):
    @abstractmethod
    def filter_users(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseCommandUserService(ABC):
    @abstractmethod
    def registration_user(self):
        raise NotImplementedError()
