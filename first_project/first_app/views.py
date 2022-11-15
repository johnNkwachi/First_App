from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.urls import reverse

todos = {
    "monday": "attend fellowship meeting",
    "tuesday": "See Banke"
}


def index(request):
    return HttpResponse("<h1>Welcome to django</>")


def nkwachi(request):
    return HttpResponse("Hello Nkwachi, welcome to django class")


def todo_by_number(request, number):
    day_list = list(todos.keys())
    day_todo = day_list[number - 1]
    redirect_path = reverse("first_app:daily-todo", args=[day_todo])
    return HttpResponseRedirect(redirect_path)


def todo(request, days):
    try:
        return HttpResponse(todos[days])
    except KeyError:
        return HttpResponse("Day not found")