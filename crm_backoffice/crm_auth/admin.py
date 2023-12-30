from django.contrib import admin

from .models import RoleUser


@admin.register(RoleUser)
class RoleAdmin(admin.ModelAdmin):
    class Meta:
        model = RoleUser
        fields = "user", "role"
