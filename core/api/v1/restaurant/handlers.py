from datetime import datetime
from logging import Logger

from rest_framework import (
    generics,
    status,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import orjson

from core.apps.common.exception import (
    CustomExceptionForApps,
    ServiceException,
)
from core.apps.restaurant.serializers.main import (
    CreateEmployeeSerializer,
    CurrentDayMenuSerializer,
    RestaurantMenuCreateSerializer,
    RestaurantTitleSerializer,
)
from core.apps.restaurant.use_cases.main import (
    CreationEmployyUseCase,
    CreationRestaurantMenuUseCase,
    CreationRestaurantUserUseCase,
    GetRestaurantMenuUseCase,
    GetRestaurantMenuUseCaseSchema,
)
from core.apps.restaurant.utils.main import IsOwner
from core.infrastructure.di.main import get_container


class RestauranCreationAPI(generics.CreateAPIView):
    serializer_class = RestaurantTitleSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer) -> Response:
        container = get_container()
        use_case: CreationRestaurantUserUseCase = container.resolve(
            CreationRestaurantUserUseCase,
        )

        try:
            result = use_case.execute(
                restaurant_data_schema=serializer.to_entity(),
            )

            return Response(
                {
                    "data": result,
                    "message": "Created successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        except ServiceException as error:
            logger: Logger = container.resolve(Logger)
            logger.error(
                msg="Error: Can't Create Restaurant",
                extra={"error_meta": orjson.dumps(error).decode()},
            )

            raise CustomExceptionForApps(
                detail=error.message,
                status_code=422,
                extra_data={"some_field": "some_value"},
            )


class RestauranUploadMenuAPI(generics.CreateAPIView):
    serializer_class = RestaurantMenuCreateSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer) -> Response:
        container = get_container()
        use_case: CreationRestaurantMenuUseCase = container.resolve(
            CreationRestaurantMenuUseCase,
        )

        try:
            result = use_case.execute(
                restaurant_menu_data_schema=serializer.to_entity(),
            )

            return Response(
                {
                    "data": result,
                    "message": "Created successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        except ServiceException as error:
            logger: Logger = container.resolve(Logger)
            logger.error(
                msg="Error: Can't Create Restaurant",
                extra={"error_meta": orjson.dumps(error).decode()},
            )

            raise CustomExceptionForApps(
                detail=error.message,
                status_code=422,
                extra_data={"some_field": "some_value"},
            )


class CreateEmployeeAPI(generics.CreateAPIView):
    serializer_class = CreateEmployeeSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer) -> Response:
        container = get_container()
        use_case: CreationEmployyUseCase = container.resolve(
            CreationEmployyUseCase,
        )

        try:
            result = use_case.execute(
                data_user_employy=serializer.to_entity(),
            )

            return Response(
                {
                    "data": result,
                    "message": "Created successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        except ServiceException as error:
            logger: Logger = container.resolve(Logger)
            logger.error(
                msg="Error: Can't Create Restaurant",
                extra={"error_meta": orjson.dumps(error).decode()},
            )

            raise CustomExceptionForApps(
                detail=error.message,
                status_code=422,
                extra_data={"some_field": "some_value"},
            )


class CurrentDayMenuAPI(generics.GenericAPIView):
    serializer_class = CurrentDayMenuSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs) -> Response:
        container = get_container()
        use_case: GetRestaurantMenuUseCase = container.resolve(
            GetRestaurantMenuUseCase,
        )

        user = request.user
        weekday = datetime.today().strftime("%A")

        schema = GetRestaurantMenuUseCaseSchema(
            user=user,
            weekday=weekday,
        )

        try:
            result = use_case.execute(
                data_user_and_weekday=schema,
            )

            return Response(
                {
                    "restaurant": result.restaurant.title,
                    "weekday": result.weekday,
                    "morning": result.morning,
                    "afternoon": result.afternoon,
                    "evening": result.evening,
                },
                status=status.HTTP_201_CREATED,
            )
        except ServiceException as error:
            logger: Logger = container.resolve(Logger)
            logger.error(
                msg="Error: Can't Create Restaurant",
                extra={"error_meta": orjson.dumps(error).decode()},
            )

            raise CustomExceptionForApps(
                detail=error.message,
                status_code=422,
                extra_data={"some_field": "some_value"},
            )
