

from audioop import reverse
from os import login_tty
from telnetlib import LOGOUT
from django.http import HttpResponseRedirect
from django.shortcuts import render
from httplib2 import Authentication


def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = Authentication(request, username=username,password=password)
        if user is not None:
            login_tty(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{
                "message":"Invalid credentials."
            })


    return render(request, "users/login.html")

def logout_view(request):
  LOGOUT(request)
  return render(request, "users/login.html",{
      "message":"logged out."
  })
  
