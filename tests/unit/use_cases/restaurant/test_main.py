from unittest.mock import Mock

import pytest

from core.apps.common.exception import ServiceException
from core.apps.restaurant.exceptions.base import BaseExceptionRestaurant
from core.apps.restaurant.exceptions.main import RestaurantAlreadyExists
from core.apps.restaurant.services.base import (
    BaseCommandRestaurantService,
    BaseQueryRestaurantService,
)
from core.apps.restaurant.use_cases.main import (
    CreationRestaurantUserUseCase,
    CreationRestaurantUserUseCaseSchema,
)


def test_restaurant_already_exists():
    # Подготовка
    query_filter_restaurant_service = Mock(BaseQueryRestaurantService)
    command_creation_restaurant_service = Mock(BaseCommandRestaurantService)

    use_case = CreationRestaurantUserUseCase(
        query_filter_restaurant_service=query_filter_restaurant_service,
        command_creation_restaurant_service=command_creation_restaurant_service,
    )

    restaurant_data_schema = CreationRestaurantUserUseCaseSchema(
        title="Test Restaurant",
    )

    # Степ 1: Mocking фильтрации
    query_filter_restaurant_service.filter_restaurant_titles.return_value = (
        True  # Чтобы симулировать, что ресторан существует
    )

    # Проверка ошибки
    with pytest.raises(RestaurantAlreadyExists):
        use_case.execute(restaurant_data_schema)


def test_successful_restaurant_creation(
    creation_restaurant_use_case,
    mock_query_service,
    mock_command_service,
):
    # Setup mock to return False (restaurant does not exist)
    mock_query_service.filter_restaurant_titles.return_value = False
    mock_command_service.creation_restaurant.return_value = (
        None  # Simulate no errors during creation
    )

    restaurant_data_schema = CreationRestaurantUserUseCaseSchema(title="New Restaurant")

    result = creation_restaurant_use_case.execute(restaurant_data_schema)

    # Assert that the result is the same as input data
    assert result.title == "New Restaurant"
    mock_query_service.filter_restaurant_titles.assert_called_once_with(
        title="New Restaurant",
    )
    mock_command_service.creation_restaurant.assert_called_once_with(
        restaurant_data=restaurant_data_schema,
    )


def test_service_exception_on_creation_error(
    creation_restaurant_use_case,
    mock_query_service,
    mock_command_service,
):
    # Setup mock to return False (restaurant does not exist)
    mock_query_service.filter_restaurant_titles.return_value = False

    # Simulate an error in restaurant creation
    mock_command_service.creation_restaurant.side_effect = BaseExceptionRestaurant(
        "Error occurred during restaurant creation",
    )

    restaurant_data_schema = CreationRestaurantUserUseCaseSchema(
        title="Restaurant with Error",
    )

    # Assert that ServiceException is raised when creation fails
    with pytest.raises(ServiceException):
        creation_restaurant_use_case.execute(restaurant_data_schema)
