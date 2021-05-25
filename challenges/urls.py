from django.urls import path

from . import views

urlpatterns = [
    path("", views.month_index),
    path("<int:month>", views.monthly_number),  # /challenges/1
    path("<str:month>", views.monthly_challenge,
         name="month-challenge")  # /challenges/january
]
