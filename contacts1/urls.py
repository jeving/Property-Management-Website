from django.urls import path

from . import views 

urlpatterns = [
    path('contact1', views.contact1, name='contact1'),
]