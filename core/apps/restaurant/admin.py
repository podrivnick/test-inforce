from django.contrib import admin

from core.apps.restaurant.models.restaurant import (
    Restaurant,
    RestaurantMenu,
)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "created_at",
        "updated_at",
    )  # Поля, которые отображаются в списке
    list_filter = ("user", "created_at")  # Фильтрация по этим полям
    search_fields = ("title",)  # Поиск по названию ресторана
    ordering = ("title",)  # Сортировка по названию ресторана

    # Если нужно, можно настроить поля для редактирования
    fieldsets = (
        (
            None,
            {
                "fields": ("title", "user"),
            },
        ),
        (
            "Dates",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )


class RestaurantMenuAdmin(admin.ModelAdmin):
    list_display = (
        "restaurant",
        "weekday",
        "morning",
        "afternoon",
        "evening",
        "created_at",
        "updated_at",
    )  # Поля, которые отображаются в списке
    list_filter = ("restaurant", "weekday")  # Фильтрация по ресторану и дню недели
    search_fields = (
        "restaurant__title",
        "weekday",
    )  # Поиск по названию ресторана и дню недели
    ordering = ("restaurant", "weekday")  # Сортировка по ресторану и дню недели

    # Настройка полей для редактирования
    fieldsets = (
        (
            None,
            {
                "fields": ("restaurant", "weekday", "morning", "afternoon", "evening"),
            },
        ),
        (
            "Dates",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )


# Регистрация моделей в админке
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantMenu, RestaurantMenuAdmin)
