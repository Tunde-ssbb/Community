from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from account.forms import RegistrationForm

# Create your views here.
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")

            account = authenticate(email=email, password=password)

            login(request, account)

            return redirect("home")
        else:
            print(form.errors)
            context["registration_form"] = form
    else: 
        form = RegistrationForm()
        context["registration_form"] = form

    context["test"] ="test"
    return render(request, "account/register.html", context)