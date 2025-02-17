from typing import Dict

from rest_framework import serializers

from core.apps.restaurant.models.restaurant import Restaurant


class RestaurantTitleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(write_only=True)

    def to_entity(self) -> Dict:
        request = self.context.get("request")
        return {
            "title": self.validated_data.get("title"),
            "user": request.user,
        }

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "title",
        ]
