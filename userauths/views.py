from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userauths import forms as userauth_forms
from doctor import models as doctor_models
from patient import models as patient_models


def register_view(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in.")
        return redirect('/')
    
    form = userauth_forms.UserRegisterForm(request.POST or None)
    
    if form.is_valid():
        user = form
        full_name = form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        user_type = form.cleaned_data.get('user_type')

        user = authenticate(request, email=email, password=password1)
        print("user =======", user)
        
        if user is not None:
            login(request, user)

            if user_type == "Doctor":
                doctor_models.Doctor.objects.create(user=user, full_name=full_name)

            else:
                patient_models.Patient.objects.create(user=user, full_name=full_name, email=email)

            messages.success(request, "Welcome, you have successfully signed up.")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials. Please try again.")


    context = {
        "form": form
    }

    return render(request, 'userauths/signup.html', context)



