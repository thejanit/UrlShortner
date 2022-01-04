from django.urls import path
from . import views

app_name = 'fuzzyurl'

urlpatterns = [
    path("", views.urlshort, name='urlshort'),
    path('u/<str:slugs>', views.redirect_url, name='redirect_url'),
]
