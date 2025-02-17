from dataclasses import (
    dataclass,
    field,
)
from typing import Any

from core.apps.common.exception import ServiceException
from core.apps.restaurant.exceptions.base import BaseExceptionRestaurant
from core.apps.restaurant.exceptions.main import RestaurantAlreadyExists
from core.apps.restaurant.services.base import (
    BaseCommandRestaurantMenuService,
    BaseCommandRestaurantService,
    BaseQueryRestaurantService,
)


@dataclass(eq=False)
class CreationRestaurantUserUseCaseSchema:
    title: str | None = field(default=None)
    user: Any | None = field(default=None)


@dataclass(eq=False)
class CreationRestaurantUserUseCase:
    query_filter_restaurant_service: BaseQueryRestaurantService
    command_creation_restaurant_service: BaseCommandRestaurantService

    def execute(
        self,
        restaurant_data_schema: CreationRestaurantUserUseCaseSchema,
    ) -> CreationRestaurantUserUseCaseSchema:
        is_restaurant_already_exist = (
            self.query_filter_restaurant_service.filter_restaurant_titles(
                title=restaurant_data_schema["title"],
            )
        )
        if is_restaurant_already_exist:
            raise RestaurantAlreadyExists()

        try:
            self.command_creation_restaurant_service.creation_restaurant(
                restaurant_data=restaurant_data_schema,
            )
        except BaseExceptionRestaurant as error:
            print(error.message)
            raise ServiceException()

        return restaurant_data_schema


@dataclass(eq=False)
class CreationRestaurantMenuUseCaseSchema:
    restaurant: str | None = field(default=None)
    weekday: str | None = field(default=None)
    morning: str | None = field(default=None)
    afternoon: str | None = field(default=None)
    evening: str | None = field(default=None)


@dataclass(eq=False)
class CreationRestaurantMenuUseCase:
    query_filter_restaurant_service: BaseQueryRestaurantService
    command_creation_restaurant_menu_service: BaseCommandRestaurantMenuService

    def execute(
        self,
        restaurant_menu_data_schema: CreationRestaurantMenuUseCaseSchema,
    ) -> CreationRestaurantMenuUseCaseSchema:
        is_restaurant_already_exist = (
            self.query_filter_restaurant_service.filter_restaurant_titles(
                title=restaurant_menu_data_schema["restaurant"],
            )
        )
        if not is_restaurant_already_exist:
            raise ValueError()

        restaurant = list(is_restaurant_already_exist)

        try:
            self.command_creation_restaurant_menu_service.creation_restaurant_menu(
                restaurant_data=restaurant_menu_data_schema,
                restaurant=restaurant,
            )
        except BaseExceptionRestaurant as error:
            print(error.message)
            raise ServiceException()

        return restaurant_menu_data_schema
