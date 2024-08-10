from django.contrib import admin
from userapp.models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "phone"]


admin.site.register(Users, UsersAdmin)
