from django.shortcuts import render, redirect
from PyDictionary import PyDictionary
from .forms import *

# Create your views here.
def a(request):
    return render(request, 'home.html')


def b(request):
    word = request.POST['search']
    obj = PyDictionary()
    meaning = obj.meaning(word)
    antonym = obj.antonym(word)
    synonym = obj.synonym(word)
    data = {
        'word': word,
        'meaning': meaning['Noun'][0],
        'antonym': antonym,
        'synonym': synonym
    }
    return render(request, 'result.html', data)


def c(request):
    if request.method=='POST':
        data=dform(request.POST)
        if data.is_valid:
            data.save()
            return redirect('/form')
    else:
        form = dform()
        print(form)
        return render(request, 'form.html', {'form': form})
