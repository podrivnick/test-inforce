from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("owner", "Власник"),
        ("worker", "Працівник"),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="worker")

    class Meta:
        db_table = "user"
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    # def to_entity(
    #     self,
    # ) -> UserSimpleEntity:
    #     return UserSimpleEntity(
    #         username=self.username,
    #         first_name=self.first_name,
    #         last_name=self.last_name,
    #         phone=self.phone,
    #     )

    def __str__(self):
        return self.username
