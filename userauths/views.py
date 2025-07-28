from django.shortcuts import render, redirect
from django.contrib.auth import messages

def register_view(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in.")
        return redirect('/')

    form = None