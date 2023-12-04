from django.urls import path,include
from .views import home,explore

urlpatterns = [
    path('',home,name="home"),
    path('explore',explore,name="explore"),
]