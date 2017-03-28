from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..log_reg.models import User
from .models import Wish

def create(request):
    return render(request, 'wish_items/create.html')

def process(request):

    if len(request.POST['item']) < 1:
        messages.add_message(request, messages.WARNING, "Item cannot be blank.")
        return redirect('/wish_items/create')
    if len(request.POST['item']) < 4:
        messages.add_message(request, messages.WARNING, "Item must be more than 3 characters.")
        return redirect('/wish_items/create')

    Wish.objects.process(request.session['user_id'], request.POST['item'])

    return redirect('/dashboard')

def feature(request, id):

    context = {

        "wishes": Wish.objects.filter(id=id),
        "users": User.objects.filter(user_wishes__id=id)
    }

    return render(request, 'wish_items/feature.html', context)

def delete(request, id):

    Wish.objects.get(id=id).delete()

    return redirect ('/dashboard')

def remove(request, id):

    user = User.objects.get(id=request.session['user_id'])
    wish = Wish.objects.get(id=id)
    wish.users.remove(user)

    return redirect ('/dashboard')

def repeatprocess(request, id):

    user = User.objects.get(id=request.session['user_id'])
    wish = Wish.objects.get(id=id)
    wish.users.add(user)

    return redirect('/dashboard')

