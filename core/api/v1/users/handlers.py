from logging import Logger

from rest_framework import (
    generics,
    status,
)
from rest_framework.response import Response

import orjson

from core.apps.common.exception import (
    CustomExceptionForUserApp,
    ServiceException,
)
from core.apps.users.serializers.main import UserSerializer
from core.apps.users.use_cases.main import RegistrationUserUseCase
from core.infrastructure.di.main import get_container


class UserRegistrationAPI(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer) -> Response:
        container = get_container()
        use_case: RegistrationUserUseCase = container.resolve(RegistrationUserUseCase)

        try:
            result = use_case.execute(
                user_data_schema=serializer.to_entity(),
            )

            return Response(
                {
                    "data": result,
                    "message": "Registered successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        except ServiceException as error:
            logger: Logger = container.resolve(Logger)
            logger.error(
                msg="User could no be registered",
                extra={"error_meta": orjson.dumps(error).decode()},
            )

            raise CustomExceptionForUserApp(
                detail=error.message,
                status_code=422,
                extra_data={"some_field": "some_value"},
            )
