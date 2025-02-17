import logging
from dataclasses import dataclass

from core.apps.restaurant.models.restaurant import Restaurant
from core.apps.restaurant.services.base import (
    BaseCommandRestaurantService,
    BaseQueryRestaurantService,
)
from core.apps.restaurant.use_cases.main import CreationRestaurantUserUseCaseSchema


@dataclass(eq=False)
class QueryRestaurantService(BaseQueryRestaurantService):
    def filter_restaurant_titles(
        self,
        title: str,
    ):
        restaurant = Restaurant.objects.filter(
            title=title,
        )
        return restaurant


@dataclass(eq=False)
class CommandRestaurantService(BaseCommandRestaurantService):
    def creation_restaurant(
        self,
        restaurant_data: CreationRestaurantUserUseCaseSchema,
    ):
        logging.info(
            f"{restaurant_data["user"]}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
        )
        Restaurant.objects.create(
            title=restaurant_data["title"],
            user=restaurant_data["user"],
        )
