from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
  path("", views.index),
  path("nkwachi/", views.nkwachi),
  path("<int:number>/", views.todo_by_number),
  path("<str:days>/", views.todo, name="daily-todo")
]
