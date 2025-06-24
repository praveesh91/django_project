from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challanges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challanges.keys())

    return render(request, "challanges/index.html", {
        "months": months
    })

def monthly_challange_by_number(request, month):
    months = list(monthly_challanges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challange", args=[redirect_month]) # /challange/january
    return HttpResponseRedirect(redirect_path)


def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        return render(request, "challanges/challange.html", {
            "text": challange_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")