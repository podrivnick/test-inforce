from django.db import models


class TimeBaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Дата створення",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата оновлення",
        auto_now=True,
    )

    class Meta:
        abstract = True
