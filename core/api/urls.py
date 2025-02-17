from django.urls import path
from rest_framework import routers

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from core.api.v1.restaurant.handlers import (
    CreateEmployeeAPI,
    RestauranCreationAPI,
    RestauranUploadMenuAPI,
)
from core.api.v1.users.handlers import UserRegistrationAPI


router = routers.SimpleRouter()

urlpatterns = [
    path("registration/", UserRegistrationAPI.as_view(), name="user-registration"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path(
        "create_restaurant/",
        RestauranCreationAPI.as_view(),
        name="restauran-creation",
    ),
    path(
        "upload_menu_restaurant/",
        RestauranUploadMenuAPI.as_view(),
        name="restauran-menu",
    ),
    path(
        "create_employy/",
        CreateEmployeeAPI.as_view(),
        name="create-employy",
    ),
]
