from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'oneimage/home_page.html')


def check_redirect(request):
    return redirect('/oneimage/results')


def check_results(request):
    return render(request, 'oneimage/results.html')
