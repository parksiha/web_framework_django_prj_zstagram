from django.contrib import admin
from django.urls import path

from users.views import login_view, logout_view,signup

# for upload image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", login_view),
    path("logout/", logout_view),
    path("signup/", signup),
]