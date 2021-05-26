from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
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
    "december": None
}


def month_index(request):
    months = list(month_ch.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_number(request, month):
    months = list(month_ch.keys())
    # response_data = render_to_string("404.html")

    if month > len(months):
        raise Http404()
    forward_to = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_to])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge = month_ch[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
