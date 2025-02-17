from dataclasses import dataclass

from core.apps.restaurant.models.restaurant import (
    Restaurant,
    RestaurantMenu,
)
from core.apps.restaurant.services.base import (
    BaseCommandRestaurantMenuService,
    BaseCommandRestaurantService,
    BaseQueryRestaurantService,
)
from core.apps.restaurant.use_cases.main import (
    CreationRestaurantMenuUseCaseSchema,
    CreationRestaurantUserUseCaseSchema,
)


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
    ) -> None:
        Restaurant.objects.create(
            title=restaurant_data["title"],
            user=restaurant_data["user"],
        )


@dataclass(eq=False)
class CommandRestaurantMenuService(BaseCommandRestaurantMenuService):
    def creation_restaurant_menu(
        self,
        restaurant_data: CreationRestaurantMenuUseCaseSchema,
        restaurant: Restaurant,
    ) -> None:
        RestaurantMenu.objects.create(
            restaurant=restaurant[0],
            weekday=restaurant_data["weekday"],
            morning=restaurant_data["morning"],
            afternoon=restaurant_data["afternoon"],
            evening=restaurant_data["evening"],
        )
