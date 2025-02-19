from django.contrib import admin

from core.apps.restaurant.models.restaurant import (
    Employee,
    MenuView,
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


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "restaurant",
        "role",
    )
    list_filter = ("restaurant", "role")
    search_fields = ("user__username", "restaurant__title")
    ordering = ("restaurant", "role")

    fieldsets = (
        (
            None,
            {
                "fields": ("user", "restaurant", "role"),
            },
        ),
    )


class MenuViewAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "menu", "user", "viewed_at")
    list_filter = ("restaurant", "menu", "viewed_at")
    search_fields = ("restaurant__title", "menu__weekday", "user__username")
    ordering = ("-viewed_at",)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantMenu, RestaurantMenuAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(MenuView, MenuViewAdmin)
