from dataclasses import dataclass

from core.apps.restaurant.config import RESTAURANT_ALREADY_EXIST_ERROR
from core.apps.restaurant.exceptions.base import BaseExceptionRestaurant


@dataclass(frozen=True)
class RestaurantAlreadyExists(BaseExceptionRestaurant):
    @property
    def message(self):
        return f"{RESTAURANT_ALREADY_EXIST_ERROR}"
