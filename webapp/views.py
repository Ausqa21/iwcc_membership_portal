from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Member, Location, Contact


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
    return render(request, "webapp/user_details.html", {"user": user})


def list_members(request):
    members = Member.objects.all()
    return render(request, "webapp/members.html", {"members": members})


def get_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, "webapp/member_details.html", {"member": member})
