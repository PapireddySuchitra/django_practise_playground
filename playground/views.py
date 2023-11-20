from django.shortcuts import render
from django.http import HttpResponse

def caluclator():
   x = 1
   y = 2

def say_hello(request):
   x = caluclator()
   return render(request, 'home.html' , {'name' : 'pichiaksh'})
# Create your views here.
