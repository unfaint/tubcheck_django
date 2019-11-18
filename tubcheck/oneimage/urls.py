from django.urls import path
from . import views

urlpatterns = [
    path('check', views.check_redirect),
    path('results', views.check_results),
]
