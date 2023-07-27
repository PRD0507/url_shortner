from django.urls import path

from . import views

urlpatterns = [
    path('shorten/<str:url>', views.shorten, name='shorten'),
    path('load_url', views.load_url, name='shorten_post')
]
