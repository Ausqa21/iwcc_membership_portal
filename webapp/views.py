from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def list_users(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "webapp/users.html", context)


def get_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    print(user.userprofile.member.first_name)
    return render(request, "webapp/user_details.html", {"user": user})
