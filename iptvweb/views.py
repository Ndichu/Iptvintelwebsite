from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def subscribe(request):
    return render(request, 'subscribe.html', {})


def subscribe2(request):
    return render(request, 'subscribe2.html', {})


def features(request):
    return render(request, 'features.html', {})

def profile(request):
    return render(request, 'myprofile.html', {})

def Dashboard(request):
    return render(request, 'dashboard.html', {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration successfull!"))
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'register_user.html', {
        'form': form,
    })


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            messages.success(
                request, ("Username or Password incorrect Please try again..."))
            # Return an 'invalid login' error message.
            return redirect('login_user')

    else:

        return render(request, 'login.html', {})


def logout(request):
    return render(request, 'home.html', {})
