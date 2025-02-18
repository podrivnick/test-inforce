from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    List,
    Optional,
)

import pytest

from core.apps.common.exception import ServiceException
from core.apps.restaurant.exceptions.base import BaseExceptionRestaurant
from core.apps.restaurant.exceptions.main import RestaurantAlreadyExists
from core.apps.restaurant.use_cases.main import (
    CreationRestaurantUserUseCase,
    CreationRestaurantUserUseCaseSchema,
)


# --- Fake Services ---
@dataclass
class FakeQueryRestaurantService:
    existing_titles: set = field(default_factory=set)

    def __post_init__(self):
        if not isinstance(self.existing_titles, set):
            self.existing_titles = set(self.existing_titles)

    def filter_restaurant_titles(self, title: str) -> bool:
        return title in self.existing_titles


@dataclass
class FakeCommandCreationRestaurantService:
    fail_title: Optional[str] = None
    store: List[str] = field(default_factory=list)

    def creation_restaurant(self, restaurant_data: Any) -> None:
        if restaurant_data.title == self.fail_title:
            raise BaseExceptionRestaurant("Creation error")
        self.store.append(restaurant_data.title)


# --- Integration Tests ---


def test_integration_successful_restaurant_creation():
    # Ресторан с таким названием ещё не существует
    fake_query = FakeQueryRestaurantService(existing_titles=[])
    fake_command = FakeCommandCreationRestaurantService()

    use_case = CreationRestaurantUserUseCase(
        query_filter_restaurant_service=fake_query,
        command_creation_restaurant_service=fake_command,
    )

    schema = CreationRestaurantUserUseCaseSchema(
        title="New Restaurant",
        user="dummy_user",
    )
    result = use_case.execute(schema)

    assert result.title == "New Restaurant"
    assert "New Restaurant" in fake_command.store


def test_integration_restaurant_already_exists():
    fake_query = FakeQueryRestaurantService(existing_titles=["Dunyasha"])
    fake_command = FakeCommandCreationRestaurantService()

    use_case = CreationRestaurantUserUseCase(
        query_filter_restaurant_service=fake_query,
        command_creation_restaurant_service=fake_command,
    )

    schema = CreationRestaurantUserUseCaseSchema(title="Dunyasha", user="dummy_user")

    with pytest.raises(RestaurantAlreadyExists):
        use_case.execute(schema)

    assert "Dunyasha" not in fake_command.store


def test_integration_creation_failure():
    fake_query = FakeQueryRestaurantService(existing_titles=[])
    fake_command = FakeCommandCreationRestaurantService(fail_title="Error Restaurant")

    use_case = CreationRestaurantUserUseCase(
        query_filter_restaurant_service=fake_query,
        command_creation_restaurant_service=fake_command,
    )

    schema = CreationRestaurantUserUseCaseSchema(
        title="Error Restaurant",
        user="dummy_user",
    )

    with pytest.raises(ServiceException):
        use_case.execute(schema)

    assert "Error Restaurant" not in fake_command.store
