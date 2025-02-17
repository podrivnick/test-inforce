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


class RestaurantMenuCreateSerializer(serializers.Serializer):
    restaurant = serializers.CharField(write_only=True)
    weekday = serializers.CharField(write_only=True)
    morning = serializers.CharField(write_only=True)
    afternoon = serializers.CharField(write_only=True)
    evening = serializers.CharField(write_only=True)

    def to_entity(self) -> Dict:
        return {
            "restaurant": self.validated_data.get("restaurant"),
            "weekday": self.validated_data.get("weekday"),
            "morning": self.validated_data.get("morning"),
            "afternoon": self.validated_data.get("afternoon"),
            "evening": self.validated_data.get("evening"),
        }
