from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    
    context = {
        'rword': get_random_string(length=14)
    }
    return render(request, 'appWord/index.html', context)

def reset(request):
    request.session['attempt'] = 0
    return redirect('/')
