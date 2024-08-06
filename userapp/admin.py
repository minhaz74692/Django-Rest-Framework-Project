from django.contrib import admin
from userapp.models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone"]


admin.site.register(Users, UsersAdmin)
