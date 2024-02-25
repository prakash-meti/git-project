from django.urls import path
from .views import get_traveller
urlpatterns = [
    path('', get_traveller),
]
