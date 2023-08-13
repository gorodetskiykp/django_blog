from django.shortcuts import render


def index(request):
    print("Hello INDEX!")
    return render(request, 'hello.html')


def today(request):
    return render(request, 'good_day.html')
