from django.urls import path
from . import views

app_name = "common"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login),
    path("logout/", views.logout),
]
