from django.shortcuts import render
from zoo.utils import *
from .models import Giraffe,Elephant,Monkey
import time


giraffes = Giraffe.objects.all()
monkeys = Monkey.objects.all()
elephants = Elephant.objects.all()


def invokeHour(request):
    print ("into invokeHour")
    implementHourProvoke()
    #instantiate
    giraffes = Giraffe.objects.all()
    monkeys = Monkey.objects.all()
    elephants = Elephant.objects.all()

    times=time.localtime()
    current_time = time.strftime("%H:%M:%S",times)
    content = {
        'giraffes': giraffes,
        'monkeys': monkeys,
        'elephants': elephants,
        'current_time':current_time
    }

    return render(request, 'zoo home page/index.html',content)
def feedZoo(request):
    commenceFeeding()

    giraffes = Giraffe.objects.all()
    monkeys = Monkey.objects.all()
    elephants = Elephant.objects.all()

    times = time.localtime()
    current_time = time.strftime("%H:%M:%S", times)
    content = {
        'giraffes': giraffes,
        'monkeys': monkeys,
        'elephants': elephants,
        'current_time':current_time
    }

    return render(request, 'zoo home page/index.html', content)
# return home page
def index(request):
    giraffes=Giraffe.objects.all()
    monkeys=Monkey.objects.all()
    elephants=Elephant.objects.all()

    times = time.localtime()
    current_time = time.strftime("%H:%M:%S", times)
    content = {
        'giraffes': giraffes,
        'monkeys': monkeys,
        'elephants': elephants,
        'current_time': current_time
    }
    return render(request,'zoo home page/index.html',content)
