from dataclasses import (
    dataclass,
    field,
)
from typing import Any

from core.apps.common.exception import ServiceException
from core.apps.restaurant.exceptions.base import BaseExceptionRestaurant
from core.apps.restaurant.exceptions.main import RestaurantAlreadyExists
from core.apps.restaurant.services.base import (
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
