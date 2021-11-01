from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.list_users, name="list_users"),
    path("users/<int:user_id>/", views.get_user, name="get_user")
]
