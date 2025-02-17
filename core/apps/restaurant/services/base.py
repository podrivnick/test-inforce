from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass(eq=False)
class BaseQueryRestaurantService(ABC):
    @abstractmethod
    def filter_restaurant_titles(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseCommandRestaurantService(ABC):
    @abstractmethod
    def creation_restaurant(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseCommandRestaurantMenuService(ABC):
    @abstractmethod
    def creation_restaurant_menu(self):
        raise NotImplementedError()
