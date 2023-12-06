from django.urls import path,include
from .views import home,explore,search,details

urlpatterns = [
    path('',home,name="home"),
    path('explore',explore,name="explore"),
    path('search/<str:para>',search,name="search"),
    path('details/<str:para>',details,name="details"),
]