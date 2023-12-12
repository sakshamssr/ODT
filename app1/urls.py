from django.urls import path,include
from .views import home,explore,search,details,about,contact,learn

urlpatterns = [
    path('',home,name="home"),
    path('explore',explore,name="explore"),
    path('search/<str:para>',search,name="search"),
    path('details/<str:bondname>/<str:para>/<str:link>/<str:para3>',details,name="details"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('learn',learn,name="learn"),
]