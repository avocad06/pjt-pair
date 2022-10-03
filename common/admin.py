from django.contrib import admin
from .models import Common


# Register your models here.
class CommonAdmin(admin.ModelAdmin):
    list_display = ("name", "password")


admin.site.register(Common)
