from django.shortcuts import render


def home_page(request):
    return render(request, 'oneimage/home_page.html')
