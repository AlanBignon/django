from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse("<h1>Hello World</h1>")


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Page des contact</h1>")


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About</h1>")


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social views</h1>")


