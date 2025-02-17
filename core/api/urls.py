from django.urls import path
from rest_framework import routers

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


router = routers.SimpleRouter()

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
