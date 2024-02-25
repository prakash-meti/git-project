from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_traveller(request):
    return HttpResponse("<h1>HI API V1</h1>")