from django.contrib import admin
from django.urls import path

from posts.views import feeds

# for upload image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("feeds/", feeds),
]