from typing import Dict

from rest_framework import serializers

from core.apps.restaurant.config import Roles_Employee
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


class CreateEmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    restaurant = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=Roles_Employee)

    def to_entity(self) -> Dict:
        return {
            "first_name": self.validated_data.get("first_name"),
            "last_name": self.validated_data.get("last_name"),
            "username": self.validated_data.get("username"),
            "password": self.validated_data.get("password"),
            "restaurant": self.validated_data.get("restaurant"),
            "role": self.validated_data.get("role"),
        }
