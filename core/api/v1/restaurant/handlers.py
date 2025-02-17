from logging import Logger

from rest_framework import (
    generics,
    status,
)
from rest_framework.response import Response

import orjson

from core.apps.common.exception import (
    CustomExceptionForApps,
    ServiceException,
)
from core.apps.restaurant.serializers.main import (
    RestaurantMenuCreateSerializer,
    RestaurantTitleSerializer,
)
from core.apps.restaurant.use_cases.main import (
    CreationRestaurantMenuUseCase,
    CreationRestaurantUserUseCase,
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
