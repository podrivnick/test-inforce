from django.db import models

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
