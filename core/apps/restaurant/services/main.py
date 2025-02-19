from dataclasses import dataclass

from core.apps.common.dependencies.user_model import User
from core.apps.restaurant.models.restaurant import (
    Employee,
    MenuView,
    Restaurant,
    RestaurantMenu,
)
from core.apps.restaurant.services.base import (
    BaseCommandMenuViewService,
    BaseCommandRestaurantMenuService,
    BaseCommandRestaurantService,
    BaseCommandUploadEmployyService,
    BaseQueryMenuViewService,
    BaseQueryRestaurantMenuService,
    BaseQueryRestaurantService,
    BaseQueryUploadEmployyService,
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

    def filter_restaurant_owners(
        self,
        user: User,
    ):
        restaurant = Restaurant.objects.filter(
            user=user,
        )
        return restaurant


@dataclass(eq=False)
class CommandRestaurantService(BaseCommandRestaurantService):
    def creation_restaurant(
        self,
        restaurant_data: CreationRestaurantUserUseCaseSchema,
    ) -> None:
        Restaurant.objects.create(
            title=restaurant_data.title,
            user=restaurant_data.user,
        )


@dataclass(eq=False)
class QueryRestaurantMenuService(BaseQueryRestaurantMenuService):
    def filter_restaurant_menu(
        self,
        restaurant: Restaurant,
    ):
        res = RestaurantMenu.objects.filter(
            restaurant=restaurant,
        )

        return res


@dataclass(eq=False)
class CommandRestaurantMenuService(BaseCommandRestaurantMenuService):
    def creation_restaurant_menu(
        self,
        restaurant_data: CreationRestaurantMenuUseCaseSchema,
        restaurant: Restaurant,
    ) -> None:
        RestaurantMenu.objects.create(
            restaurant=restaurant[0],
            weekday=restaurant_data.weekday,
            morning=restaurant_data.morning,
            afternoon=restaurant_data.afternoon,
            evening=restaurant_data.evening,
        )


@dataclass(eq=False)
class QueryUploadEmployyService(BaseQueryUploadEmployyService):
    def get_employy(
        self,
        user: User,
    ) -> Employee:
        employy = Employee.objects.filter(
            user=user,
        ).first()

        return employy


@dataclass(eq=False)
class CommandUploadEmployyService(BaseCommandUploadEmployyService):
    def create_employy(
        self,
        user: User,
        restaurant: Restaurant,
        role: str,
    ) -> None:
        Employee.objects.create(
            user=user,
            restaurant=restaurant[0],
            role=role,
        )


@dataclass(eq=False)
class QueryMenuViewService(BaseQueryMenuViewService):
    def filter_menu_views_by_restaurant(
        self,
        restaurant: Restaurant,
        weekday: str,
    ):
        menu_statistics = MenuView.objects.filter(
            restaurant=restaurant,
            viewed_at__date=weekday,
        )

        return menu_statistics


@dataclass(eq=False)
class CommandMenuViewService(BaseCommandMenuViewService):
    def create_viewed_menu(
        self,
        restaurant: Restaurant,
        user: User,
        menu: RestaurantMenu,
    ):
        MenuView.objects.create(
            restaurant=restaurant,
            menu=menu,
            user=user,
        )
