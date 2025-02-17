from django.contrib.auth.models import (
    AbstractUser,
    Group,
    Permission,
)
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("owner", "Власник"),
        ("worker", "Працівник"),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="worker")

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
    )

    class Meta:
        db_table = "user"
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def __str__(self):
        return self.username
