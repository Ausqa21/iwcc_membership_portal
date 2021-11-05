from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.list_users, name="list_users"),
    path("users/<int:user_id>/", views.get_user, name="get_user"),
    path("members/", views.list_members, name="list_members"),
    path("members/<int:member_id>/", views.get_member, name="get_member")
]
