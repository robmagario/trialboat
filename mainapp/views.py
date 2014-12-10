from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from mainapp import models


@login_required
def home(request):
    orders = models.Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, "home.html", context)


def register(request):
    context = {}
    return render(request, "register.html", context)