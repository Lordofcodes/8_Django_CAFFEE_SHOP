from django.contrib.auth import login, logout, get_user_model
from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from .forms import UserForm
from .models import Coffee
from .utils import *


def home(request):
    return render(request, "home/home.html")


def signup(request):
    if request.method == 'POST':
        print('POST  ' * 20)
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            print('GET METHOD ' * 20)
            return redirect('home:index')

    else:
        form = UserForm()
        print('IT WORKS ' * 20)
        return render(request, 'home/signup.html', {'form': form})


def place_order(request):
    OrderFormSet = modelformset_factory(Coffee, fields=["name", "size", "quantity"], max_num=2, extra=3,
                                       validate_max=True, can_delete=True)
    #tworzenie klasy w fabryce

    user = get_user_model().objects.get(username=request, instance=username)

    if request.method == "POST":
        order_formset = OrderFormSet(request.POST)
        if order_formset.is_valid():
            order_formset.save()
            return redirect('home:index')
    else:
        data = {
            'form-TOTAL_FORMS': 3,
            'form-INITIAL_FORMS': 3,
            'form-0-name': AMERICANO,
            'form-0-quantity': '1',
            'form-0-size': LARGE,
            'form-1-name': AMERICANO,
            'form-1-quantity': '1',
            'form-1-size': LARGE,
            'form-2-name': AMERICANO,
            'form-2-quantity': '1',
            'form-2-size': LARGE,
        }
        order_formset = OrderFormSet(
            data,
            queryset=Coffee.objects.none()
        ) #zwracanie pustego queryseta modelu coffee

    return render(request, 'home/order.html', {'formset': order_formset})


def logout_user(request):
    logout(request)
    return redirect('home:index')
