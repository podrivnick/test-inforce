from unittest.mock import MagicMock

import pytest

from core.apps.restaurant.services.base import (
    BaseCommandRestaurantService,
    BaseQueryRestaurantService,
)
from core.apps.restaurant.use_cases.main import CreationRestaurantUserUseCase


@pytest.fixture
def query_service_mock():
    return MagicMock(spec=BaseQueryRestaurantService)


@pytest.fixture
def command_service_mock():
    return MagicMock(spec=BaseCommandRestaurantService)


@pytest.fixture
def use_case(query_service_mock, command_service_mock):
    return CreationRestaurantUserUseCase(
        query_filter_restaurant_service=query_service_mock,
        command_creation_restaurant_service=command_service_mock,
    )
