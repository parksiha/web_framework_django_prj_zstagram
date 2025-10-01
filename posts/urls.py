from django.contrib import admin
from django.urls import path

from posts.views import feeds, feed_detail, comment_add

# for upload image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("feeds/", feeds),
    path("comment_add/", comment_add),
    path("<int:post_id>/", feed_detail),
]