from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import LINK
from .forms import linkform
from django.contrib.auth.decorators import login_required
from users.models import User
from django.db import IntegrityError


# Create your views here.
@login_required
def index(request: HttpRequest):
    username = request.user.username
    user = get_object_or_404(User, username=username)
    if request.method == "GET":
        link_form = linkform()

    elif request.method == "POST":
        link_form = linkform(request.POST)
        if link_form.is_valid():
            link_url = link_form.cleaned_data["add_link"]
            link_name = link_form.cleaned_data["add_name"]

            my_link = LINK.objects.filter(name = link_url)
            if(my_link):
                my_link[0].user.add(request.user)
            else:
                my_link = LINK.objects.create(url=link_url, name=link_name)
                my_link.user.add(request.user)
                my_link.save()

    return render(
        request,
        "index/index.html",
        context={"links": LINK.objects.filter(user=request.user)},
    )
