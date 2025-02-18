from dataclasses import dataclass

from core.apps.restaurant.config import BASE_EXCEPTION_RESTAURANT


@dataclass(eq=False)
class BaseExceptionRestaurant(Exception):
    product: int = None

    @property
    def message(self):
        return BASE_EXCEPTION_RESTAURANT
