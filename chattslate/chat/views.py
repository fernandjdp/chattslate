from django.shortcuts import render
from .models import Room
# Create your views here.
# 

'''rooms = [
    {'id':1, 'name': 'Sala 1', 'codigo': 'abcde'},
    {'id':2, 'name': 'Sala 2', 'codigo': 'fghij'},
    {'id':3, 'name': 'Sala 3', 'codigo': 'klmnñ'},
    {'id':4, 'name': 'Sala 4', 'codigo': 'opqrs'},
]'''

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'chat/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}

    return render(request, 'chat/room.html', context)

def create_room(request):
    context = {}
    return render(request, 'chat/room_form.html', context)