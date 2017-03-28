from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from ..wish_items.models import Wish


def index(request):
    return redirect('/main')

def main(request):
    return render(request, 'log_reg/index.html')

def login(request):

    result = User.objects.login(request.POST.copy())
    if 'errors' in result:
        for error in result['errors']:
            messages.add_message(request, messages.ERROR, error)

        return redirect('/')
    request.session['user'] = result['user'].first_name
    request.session['action'] = 'login'
    request.session['user_id'] = result['user'].id

    return redirect('/dashboard')

def register(request):

    result = User.objects.register(request.POST.copy())

    if 'errors' in result:
        for error in result['errors']:
            messages.add_message(request, messages.ERROR, error)

        return redirect('/')
    request.session['user'] = result['user'].first_name
    request.session['action'] = 'register'
    request.session['user_id'] = result['user'].id

    return redirect('/dashboard')

def logout(request):

    request.session.clear()
    return redirect('/')

def dashboard(request):

    id = request.session['user_id']
    x = User.objects.get(id=id)

    context = {
        "my_wishes": Wish.objects.filter(users=x),
        "other_wishes": Wish.objects.exclude(users=x),
    }

    return render(request, 'log_reg/dashboard.html', context)


