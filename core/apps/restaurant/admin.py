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
    )
    list_filter = ("user", "created_at")
    search_fields = ("title",)
    ordering = ("title",)

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

    readonly_fields = ("created_at", "updated_at")


class RestaurantMenuAdmin(admin.ModelAdmin):
    list_display = (
        "restaurant",
        "weekday",
        "morning",
        "afternoon",
        "evening",
        "created_at",
        "updated_at",
    )
    list_filter = ("restaurant", "weekday")
    search_fields = (
        "restaurant__title",
        "weekday",
    )
    ordering = ("restaurant", "weekday")

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

    readonly_fields = ("created_at", "updated_at")


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantMenu, RestaurantMenuAdmin)
