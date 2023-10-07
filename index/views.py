from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import LINK
from .forms import linkform, Deletelinkform
from django.contrib.auth.decorators import login_required
from users.models import User
from django.db import IntegrityError


# Create your views here.
@login_required
def index(request: HttpRequest):
    username = request.user.username
    user = get_object_or_404(User, username=username)
    wrong_message = ""
    if request.method == "POST":
        link_form = linkform(request.POST)
        deletelinkform = Deletelinkform(request.POST, request.FILES)
        if link_form.is_valid():
            link_url = link_form.cleaned_data["add_link"]
            link_name = link_form.cleaned_data["add_name"]
            if not link_url.startswith("https://"):
                link_url = "https://" + link_url
            my_link = LINK.objects.filter(url=link_url)
            if my_link:
                try:
                    my_link[0].user.add(request.user)
                except:
                    wrong_message = "The name of this link already exists"
            else:
                my_link = LINK.objects.create(url=link_url, name=link_name)
                my_link.user.add(request.user)
                my_link.save()
        if deletelinkform.is_valid():
            link_name = deletelinkform.cleaned_data["delete_name"]
            my_link = LINK.objects.filter(name=link_name)
            if my_link:
                my_link[0].user.remove(request.user)
            else:
                wrong_message = "The name of this link doen't exist"


    return render(
        request,
        "index/index.html",
        context={"links": LINK.objects.filter(user=request.user)},
    )
