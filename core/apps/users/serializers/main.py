from typing import Dict

from rest_framework import serializers

from core.apps.common.config import ROLES
from core.apps.common.dependencies.user_model import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=ROLES)

    def to_entity(self) -> Dict:
        return {
            "first_name": self.validated_data.get("first_name"),
            "last_name": self.validated_data.get("last_name"),
            "username": self.validated_data.get("username"),
            "password": self.validated_data.get("password"),
            "role": self.validated_data.get("role"),
        }

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "role",
            "first_name",
            "last_name",
        ]
