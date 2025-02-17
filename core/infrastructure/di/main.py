from functools import lru_cache
from logging import (
    getLogger,
    Logger,
)

import punq

from core.apps.users.services.base import (
    BaseCommandUserService,
    BaseQueryUserService,
)
from core.apps.users.services.main import (
    CommandUserService,
    QueryUserService,
)
from core.apps.users.use_cases.main import RegistrationUserUseCase


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # init internal stuff
    container.register(Logger, factory=getLogger, name="apm-server")

    # init services
    container.register(BaseQueryUserService, QueryUserService)
    container.register(BaseCommandUserService, CommandUserService)

    # init use cases
    container.register(RegistrationUserUseCase)

    return container
