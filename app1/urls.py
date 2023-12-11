from django.urls import path,include
from .views import home,explore,search,details,about

urlpatterns = [
    path('',home,name="home"),
    path('explore',explore,name="explore"),
    path('search/<str:para>',search,name="search"),
    path('details/<str:bondname>/<str:para>/<str:para2>/<str:para3>',details,name="details"),
    path('about',about,name="about"),
]