# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.apps.users.models.users import User


@admin.register(User)
class UserAdministration(UserAdmin):
    search_fields = ["username"]
    list_filter = ["is_active", "is_superuser"]
    list_display = [
        "username",
        "is_active",
        "is_superuser",
        "date_joined",
        "role",
    ]
    ordering = ["-date_joined"]
    readonly_fields = ["last_login", "date_joined"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("first_name", "last_name", "role")},
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_superuser", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
