import logging
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
    BaseCommandUploadEmployyService,
    BaseQueryRestaurantMenuService,
    BaseQueryRestaurantService,
    BaseQueryUploadEmployyService,
)
from core.apps.users.excaptions.base import BaseExceptionUser
from core.apps.users.excaptions.main import UserAlreadyExists
from core.apps.users.services.base import (
    BaseCommandUserService,
    BaseQueryUserService,
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


@dataclass(eq=False)
class CreationEmployyUseCaseSchema:
    role: str | None = field(default=None)
    first_name: str | None = field(default=None)
    last_name: str | None = field(default=None)
    username: str | None = field(default=None)
    password: str | None = field(default=None)
    restaurant: str | None = field(default=None)
    work_role: str | None = field(default=None)


@dataclass(eq=False)
class CreationEmployyUseCase:
    query_filter_restaurant_service: BaseQueryRestaurantService
    query_filter_user_service: BaseQueryUserService
    command_register_user_service: BaseCommandUserService
    command_creation_employy_service: BaseCommandUploadEmployyService

    def execute(
        self,
        data_user_employy: CreationEmployyUseCaseSchema,
    ) -> CreationEmployyUseCaseSchema:
        is_restaurant_already_exist = (
            self.query_filter_restaurant_service.filter_restaurant_titles(
                title=data_user_employy["restaurant"],
            )
        )
        if not is_restaurant_already_exist:
            raise ValueError()

        restaurant = list(is_restaurant_already_exist)

        is_user_already_exist = self.query_filter_user_service.filter_users(
            username=data_user_employy["username"],
        )
        if is_user_already_exist:
            raise UserAlreadyExists()

        try:
            user = self.command_register_user_service.registration_user(
                user_data=data_user_employy,
            )
        except BaseExceptionUser as error:
            print(error.message)
            raise ServiceException()

        try:
            self.command_creation_employy_service.create_employy(
                user=user,
                restaurant=restaurant,
                role=data_user_employy["work_role"],
            )
        except BaseExceptionRestaurant as error:
            print(error.message)
            raise ServiceException()

        return data_user_employy


@dataclass(eq=False)
class GetRestaurantMenuUseCaseSchema:
    user: Any | None = field(default=None)
    weekday: str | None = field(default=None)


@dataclass(eq=False)
class GetRestaurantMenuUseCase:
    query_filter_employees_service: BaseQueryUploadEmployyService
    query_filter_restaurant_menu_service: BaseQueryRestaurantMenuService
    query_filter_restaurant_service: BaseQueryRestaurantService

    def execute(
        self,
        data_user_and_weekday: GetRestaurantMenuUseCaseSchema,
    ) -> GetRestaurantMenuUseCaseSchema:
        if data_user_and_weekday.user.role == "Працівник":
            employy = self.query_filter_employees_service.get_employy(
                user=data_user_and_weekday.user,
            )
            logging.info(f"{employy.restaurant}!!!!!!!!!!!!!!!!!!!!!")
            restaurant_menu = (
                self.query_filter_restaurant_menu_service.filter_restaurant_menu(
                    restaurant=employy[0].restaurant,
                )
            )
        elif data_user_and_weekday.user.role == "Власник":
            restaurant = self.query_filter_restaurant_service.filter_restaurant_owners(
                user=data_user_and_weekday.user,
            )
            restaurant_menu = (
                self.query_filter_restaurant_menu_service.filter_restaurant_menu(
                    restaurant=restaurant,
                )
            )
        updated_restaurant_menu = list(restaurant_menu)

        filtered_restaurant_menu = self.filter_results_restaurant_menu(
            restaurant_menu=updated_restaurant_menu,
            weekday=data_user_and_weekday.weekday,
        )

        logging.info(f"{filtered_restaurant_menu}!!!!!!!!!!!!!!!!!!!!!")

        return filtered_restaurant_menu[0]

    @staticmethod
    def filter_results_restaurant_menu(restaurant_menu, weekday):
        filtered_weekday = [e for e in restaurant_menu if e.weekday == weekday]

        return filtered_weekday
