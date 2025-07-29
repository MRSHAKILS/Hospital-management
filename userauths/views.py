from django.shortcuts import render, redirect
from django.contrib import messages
from userauths import forms as userauth_forms

def register_view(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in.")
        return redirect('/')

    form = userauth_forms.UserRegisterForm()
    context = {
        "form": form
    }

    return render(request, 'userauths/signup.html', context)