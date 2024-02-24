from django.urls import path
from .views import show_home_page
urlpatterns = [
    path('home/', show_home_page),
]
