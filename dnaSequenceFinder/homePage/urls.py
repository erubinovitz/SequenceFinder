from django.urls import path
from homePage import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    #path("<int:pk>/", views.submissionDetail, name="submissionDetail"),
]
