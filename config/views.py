# core/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Jaza Savings App!</h1>")
