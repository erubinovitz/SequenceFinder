from django.urls import path
from . import views

urlpatterns = [

    path("", views.searchHistoryIndex, name="searchHistoryIndex"),
]
