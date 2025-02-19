from django.db import models
from django.utils import timezone

from core.apps.common.models import TimeBaseModel
from core.apps.users.models.user import User


class Restaurant(TimeBaseModel):
    title = models.CharField(max_length=50, verbose_name="Назва Ресторану", null=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        null=False,
        verbose_name="Власник",
        blank=False,
    )

    class Meta:
        db_table = "restaurant"
        verbose_name = "Ресторан"
        verbose_name_plural = "Ресторани"


class RestaurantMenu(TimeBaseModel):
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.PROTECT,
        null=False,
        verbose_name="Ресторан",
        blank=False,
    )
    weekday = models.CharField(max_length=50, verbose_name="День Тижня", null=False)
    morning = models.CharField(max_length=50, verbose_name="Ранок", null=False)
    afternoon = models.CharField(max_length=50, verbose_name="Опівдні", null=False)
    evening = models.CharField(max_length=50, verbose_name="Вечір", null=False)

    class Meta:
        db_table = "menu"
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuView(models.Model):
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
        verbose_name="Ресторан",
    )
    menu = models.ForeignKey(
        to=RestaurantMenu,
        on_delete=models.CASCADE,
        verbose_name="Меню",
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Користувач",
    )
    viewed_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата перегляду",
    )

    class Meta:
        verbose_name = "Перегляд меню"
        verbose_name_plural = "Перегляди меню"

    def __str__(self):
        return (
            f"{self.restaurant.title} - {self.menu.weekday} viewed at {self.viewed_at}"
        )


class Employee(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant,
        related_name="employees",
        on_delete=models.CASCADE,
    )
    role = models.CharField(
        max_length=50,
        choices=[("chef", "Chef"), ("waiter", "Waiter")],
    )

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    class Meta:
        db_table = "employee"
        verbose_name = "Співробітники"
        verbose_name_plural = "Співробітники"
