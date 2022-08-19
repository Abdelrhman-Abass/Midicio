
from . import views
from django.urls import path 


urlpatterns = [
    path('', views.makeapointment, name='makeapointment'),
]
