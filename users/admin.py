from django.contrib import admin

from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'avatar',)
    list_filter = ('gender', )


admin.site.register(CustomUser, CustomUserAdmin)
