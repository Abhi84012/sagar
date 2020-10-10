from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('person', views.person, name="person"),
    path('persondetail', views.persondetail, name="persondetail"),
    
]