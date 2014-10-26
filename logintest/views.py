from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout



def logout(request):
    """Logs out user"""
    auth_logout(request)
    response = redirect('/')
    response.delete_cookie("csrftoken")
    response.delete_cookie("sessionid")
    return response


def root(request):
    return render(request, "index.html")


def done(request):
    return render(request, "index.html")
