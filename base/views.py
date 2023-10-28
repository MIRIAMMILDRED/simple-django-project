from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.
rooms =[
   { 'id':1 , 'name':'learn Django'},
     { 'id':2 , 'name':'Design with me'},
     { 'id':3 , 'name':'frontend developers'},
]



def home(request):
    rooms = Room.objects.all()
    dictonary = {'rooms':rooms}
    return render(request, 'base/index.html',dictonary )

def root(request, pk):
    return render(request , 'base/root.html',{'rooms':rooms})