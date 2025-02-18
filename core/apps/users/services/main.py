from dataclasses import dataclass

from core.apps.common.dependencies.user_model import User
from core.apps.restaurant.use_cases.main import CreationEmployyUseCaseSchema
from core.apps.users.services.base import (
    BaseCommandUserService,
    BaseQueryUserService,
)
from core.apps.users.use_cases.main import RegistrationUserUseCaseSchema


@dataclass(eq=False)
class QueryUserService(BaseQueryUserService):
    def filter_users(
        self,
        username: str,
    ):
        user = User.objects.filter(
            username=username,
        )
        return user


@dataclass(eq=False)
class CommandUserService(BaseCommandUserService):
    def registration_user(
        self,
        user_data: RegistrationUserUseCaseSchema | CreationEmployyUseCaseSchema,
    ):
        user = User.objects.create_user(
            username=user_data.username,
            password=user_data.password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            role=user_data.role,
        )

        return user
