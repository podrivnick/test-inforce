from django.contrib.auth import get_user_model


class UserService:
    """Because we use an Abstract class in the User model."""

    _user_model = None

    @classmethod
    def get_user_model(cls):
        if cls._user_model is None:
            cls._user_model = get_user_model()
        return cls._user_model


User = UserService.get_user_model()
