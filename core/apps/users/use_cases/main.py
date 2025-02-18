from dataclasses import (
    dataclass,
    field,
)

from core.apps.common.exception import ServiceException
from core.apps.users.excaptions.base import BaseExceptionUser
from core.apps.users.excaptions.main import UserAlreadyExists
from core.apps.users.services.base import (
    BaseCommandUserService,
    BaseQueryUserService,
)


@dataclass(eq=False)
class RegistrationUserUseCaseSchema:
    first_name: str | None = field(default=None)
    last_name: str | None = field(default=None)
    username: str | None = field(default=None)
    password: str | None = field(default=None)
    role: str | None = field(default=None)


@dataclass(eq=False)
class RegistrationUserUseCase:
    query_filter_user_service: BaseQueryUserService
    command_register_user_service: BaseCommandUserService

    def execute(
        self,
        user_data_schema: RegistrationUserUseCaseSchema,
    ) -> RegistrationUserUseCaseSchema:
        is_user_already_exist = self.query_filter_user_service.filter_users(
            username=user_data_schema.username,
        )
        if is_user_already_exist:
            raise UserAlreadyExists()

        try:
            self.command_register_user_service.registration_user(
                user_data=user_data_schema,
            )
        except BaseExceptionUser as error:
            print(error.message)
            raise ServiceException()

        return user_data_schema
