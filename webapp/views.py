from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def list_users(request):
    users = User.objects.all()
    for user in users:
        print(user.member)
    return HttpResponse(users)
