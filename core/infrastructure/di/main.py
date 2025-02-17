from functools import lru_cache
from logging import (
    getLogger,
    Logger,
)

import punq

from core.apps.restaurant.services.base import (
    BaseCommandRestaurantMenuService,
    BaseCommandRestaurantService,
    BaseQueryRestaurantService,
)
from core.apps.restaurant.services.main import (
    CommandRestaurantMenuService,
    CommandRestaurantService,
    QueryRestaurantService,
)
from core.apps.restaurant.use_cases.main import (
    CreationRestaurantMenuUseCase,
    CreationRestaurantUserUseCase,
)
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
    container.register(BaseQueryRestaurantService, QueryRestaurantService)
    container.register(BaseCommandRestaurantService, CommandRestaurantService)
    container.register(BaseCommandRestaurantMenuService, CommandRestaurantMenuService)

    # init use cases
    container.register(RegistrationUserUseCase)
    container.register(CreationRestaurantUserUseCase)
    container.register(CreationRestaurantMenuUseCase)

    return container
