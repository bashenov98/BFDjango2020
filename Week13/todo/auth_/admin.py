from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_.models import CustomUser, Profile


@admin.register(CustomUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )




@admin.register(Profile)
class MyProfile(admin.ModelAdmin):
    list_display = ('user', 'bio', 'address')