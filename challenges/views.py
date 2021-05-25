from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

month_ch = {
    "january": "Walk 500 miles",
    "february": "Run 500 miles",
    "march": "Swim everyday",
    "april": "Workout abs",
    "may": "Sleep at least 6 hours",
    "june": "Read 50 Books",
    "july": "Sleep",
    "august": "Do Nothing",
    "september": "Dance with youself",
    "october": "Eat a fruit everyday",
    "november": "Spend money on things you don't need",
    "december": "Create a hip hop album",
}


def month_index(request):
    list_items = ""
    months = list(month_ch.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.title()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_number(request, month):
    months = list(month_ch.keys())

    if month > len(months):
        return HttpResponseNotFound("Month Not Supported")
    forward_to = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_to])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge = month_ch[month]
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("Month Not Supported")
