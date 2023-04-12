from django.shortcuts import render, HttpResponse

# Create your views here.
def MainView(request):
    return HttpResponse("Congratulations!")