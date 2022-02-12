from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from .forms import UserForm


# Create your views here.
from .models import Coffee


def home(request):
    return render(request, "home/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:index')

    else:
        form = UserForm()
    return render(request, 'home/signup.html', {
        "form": form
    })


def place_order(request):
    OrderFormSet = modelformset_factory(Coffee, fields=['name', 'size', 'quantity'], max_num=2, extra=3)

    if request.method == 'POST':
        order_formset = OrderFormSet(request.POST)
        if order_formset.is_valid():
            order_formset.save()
            return redirect('home:index')
    else:
        order_formset = OrderFormSet

    return render(request, 'home/order.html', {'formset': order_formset})

