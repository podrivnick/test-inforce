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

    @abstractmethod
    def filter_restaurant_owners(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseCommandRestaurantService(ABC):
    @abstractmethod
    def creation_restaurant(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseQueryRestaurantMenuService(ABC):
    @abstractmethod
    def filter_restaurant_menu(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseCommandRestaurantMenuService(ABC):
    @abstractmethod
    def creation_restaurant_menu(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseQueryUploadEmployyService(ABC):
    @abstractmethod
    def get_employy(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseCommandUploadEmployyService(ABC):
    @abstractmethod
    def create_employy(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseCommandMenuViewService(ABC):
    @abstractmethod
    def create_viewed_menu(self):
        raise NotImplementedError()


@dataclass(eq=False)
class BaseQueryMenuViewService(ABC):
    @abstractmethod
    def filter_menu_views_by_restaurant(self):
        raise NotImplementedError()
