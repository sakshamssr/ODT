from django.urls import path,include
from .views import home,explore,search

urlpatterns = [
    path('',home,name="home"),
    path('explore',explore,name="explore"),
    path('search/<str:para>',search,name="search"),
]