from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.


def monthly_challenge(request, month):
    challenge = None
    if month == "january":
        challenge = "Sleep All Day"
    elif month == "february":
        challenge = "Dance on you hands"
    else:
        return HttpResponseNotFound("Page not found")
    return HttpResponse(challenge)
