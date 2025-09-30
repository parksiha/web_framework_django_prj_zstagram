from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "password")}),
        ("개인정보", {"fields": ("first_name", "last_name", "email")}),
        ("추가필드", {"fields": ("profile_image", "short_description")}),
        ("권한", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("일자", {"fields": ("last_login", "date_joined")}),
    ]

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "profile_image", "short_description"),
        }),
    )

    list_display = ("username", "email", "first_name", "last_name", "profile_image", "short_description", "is_staff")