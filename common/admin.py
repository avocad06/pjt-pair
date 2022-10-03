from django.contrib import admin

# Register your models here.
class CommonAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')