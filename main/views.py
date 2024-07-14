from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.

def index(request):
    data = {
        'title': 'he.xi',
        'values': ['Lorem','Ipsum', '1488 ']
    }
    return render(request, 'main/index.html', data)

def cr4d(request):
    return render(request, 'main/cr4d.html')

def whenisnextvideo(request):
    return render(request, 'main/whenisnextvideo.html')

def gd(request):
    return render(request, 'main/gd.html')

def r(request):
    string = ''
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+-=|/.'
    for i in range(100000):
        string += choice(letters)
    return HttpResponse(string)

def info(request):
    data = {
        'title': 'he.xi',
        'levels': ['Globed Collisions','Stereo TPLL','is it a bug','Fire and the hole','PODWALL','BIRAL','Test your luck'],
        'levelsDict': {
            'Globed Collision': [107100851, 'Уровень для коллизий в Глобед'],
            'Stereo TPLL': [104616243, 'Почти самый сложный уровень во вселенной'],
            'is it a bug': [101925532, 'Я нашёл баг и решил его всем показать'],
            'Fire and the hole': [99132690, 'Все вариации звука "Fire in the hole"'],
            'PODWALL': [97832873, 'Задумывалось, что он получит рейт'],
            'BIRAL': [95590358, 'Этот уровень также должен быть с декором и на рейт, но я сделал только ГП'],
            'Test your luck': [93680214, 'Шанс пройти этот уровень 0%']
        }
    }
    return render(request, 'main/info.html', data)

def database(request):
    return render(request, 'main/database.html')

def about(request):
    return render(request, 'main/about.html')

def cr4drules(request):
    return render(request, 'main/cr4drules.html')

def cr4drulesop(request):
    return render(request, 'main/cr4drulesop.html')

def cr4dbuildings(request):
    return render(request, 'main/cr4dbuildings.html')

def cr4dhistory(request):
    return render(request, 'main/cr4dhistory.html')

def nextlevel(request):
    return render(request, 'main/whenisnextlevel.html')

def hexi(request):
    return render(request, 'main/hexi.html')

def sociallinks(request):
    return render(request, 'main/sociallinks.html')

def hexiqna(request):
    return render(request, 'main/hexiqna.html')

def maininfo(request):
    return render(request, 'main/maininfo.html')