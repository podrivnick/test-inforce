from functools import lru_cache
from logging import (
    getLogger,
    Logger,
)

import punq

from core.apps.restaurant.services.base import (
    BaseCommandMenuViewService,
    BaseCommandRestaurantMenuService,
    BaseCommandRestaurantService,
    BaseCommandUploadEmployyService,
    BaseQueryMenuViewService,
    BaseQueryRestaurantMenuService,
    BaseQueryRestaurantService,
    BaseQueryUploadEmployyService,
)
from core.apps.restaurant.services.main import (
    CommandMenuViewService,
    CommandRestaurantMenuService,
    CommandRestaurantService,
    CommandUploadEmployyService,
    QueryMenuViewService,
    QueryRestaurantMenuService,
    QueryRestaurantService,
    QueryUploadEmployyService,
)
from core.apps.restaurant.use_cases.main import (
    CreationEmployyUseCase,
    CreationRestaurantMenuUseCase,
    CreationRestaurantUserUseCase,
    GetRestaurantMenuUseCase,
    GetRestaurantStatisticsUseCase,
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
    container.register(BaseCommandUploadEmployyService, CommandUploadEmployyService)
    container.register(BaseQueryRestaurantMenuService, QueryRestaurantMenuService)
    container.register(BaseQueryUploadEmployyService, QueryUploadEmployyService)
    container.register(BaseQueryMenuViewService, QueryMenuViewService)
    container.register(BaseCommandMenuViewService, CommandMenuViewService)

    # init use cases
    container.register(RegistrationUserUseCase)
    container.register(CreationRestaurantUserUseCase)
    container.register(CreationRestaurantMenuUseCase)
    container.register(CreationEmployyUseCase)
    container.register(GetRestaurantMenuUseCase)
    container.register(GetRestaurantStatisticsUseCase)

    return container
