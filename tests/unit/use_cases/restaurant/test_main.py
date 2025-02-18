import pytest

from core.apps.common.exception import ServiceException
from core.apps.restaurant.exceptions.base import BaseExceptionRestaurant
from core.apps.restaurant.exceptions.main import RestaurantAlreadyExists
from core.apps.restaurant.use_cases.main import CreationRestaurantUserUseCaseSchema


# Тест: ресторан із цією назвою вже існує
def test_restaurant_already_exists(use_case, query_service_mock):
    schema = CreationRestaurantUserUseCaseSchema(
        title="Test Restaurant",
        user="dummy_user",
    )

    query_service_mock.filter_restaurant_titles.return_value = True

    with pytest.raises(RestaurantAlreadyExists):
        use_case.execute(schema)

    query_service_mock.filter_restaurant_titles.assert_called_once_with(
        title=schema.title,
    )


# Тест: успішне створення ресторану, якщо його ще немає
def test_successful_restaurant_creation(
    use_case,
    query_service_mock,
    command_service_mock,
):
    schema = CreationRestaurantUserUseCaseSchema(
        title="New Restaurant",
        user="dummy_user",
    )

    query_service_mock.filter_restaurant_titles.return_value = False

    command_service_mock.creation_restaurant.return_value = None

    result = use_case.execute(schema)

    assert result == schema
    query_service_mock.filter_restaurant_titles.assert_called_once_with(
        title=schema.title,
    )
    command_service_mock.creation_restaurant.assert_called_once_with(
        restaurant_data=schema,
    )


# Тест: якщо при створенні ресторану відбувається помилка, має бути викинуто ServiceException
def test_service_exception_on_creation_error(
    use_case,
    query_service_mock,
    command_service_mock,
):
    schema = CreationRestaurantUserUseCaseSchema(
        title="Error Restaurant",
        user="dummy_user",
    )

    query_service_mock.filter_restaurant_titles.return_value = False
    command_service_mock.creation_restaurant.side_effect = BaseExceptionRestaurant(
        "Creation error",
    )

    with pytest.raises(ServiceException):
        use_case.execute(schema)

    query_service_mock.filter_restaurant_titles.assert_called_once_with(
        title=schema.title,
    )
    command_service_mock.creation_restaurant.assert_called_once_with(
        restaurant_data=schema,
    )
