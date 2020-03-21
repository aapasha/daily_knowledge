from django.shortcuts import render


def home(request):
    return render(request, 'spiritual_treasures/home.html', {'title': 'Home'})
