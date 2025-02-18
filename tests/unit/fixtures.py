from unittest.mock import MagicMock

import pytest

from core.apps.restaurant.services.base import (
    BaseCommandRestaurantService,
    BaseQueryRestaurantService,
)
from core.apps.restaurant.use_cases.main import CreationRestaurantUserUseCase


@pytest.fixture
def mock_query_service():
    return MagicMock(BaseQueryRestaurantService)


@pytest.fixture
def mock_command_service():
    return MagicMock(BaseCommandRestaurantService)


@pytest.fixture
def creation_restaurant_use_case(mock_query_service, mock_command_service):
    return CreationRestaurantUserUseCase(
        query_filter_restaurant_service=mock_query_service,
        command_creation_restaurant_service=mock_command_service,
    )
