from django.urls import path

from . import views

urlpatterns = [
    path('shorten', views.shorten_post, name='shorten_post'),
    path('shorten/<str:url>', views.shorten, name='shorten'),
]