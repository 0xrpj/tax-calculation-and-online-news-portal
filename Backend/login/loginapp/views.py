from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 
from .models import Post
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , DetailView


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'loginapp/Html file/Register.html', context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Email OR password is incorrect')
                return redirect('login')
        context = {}
        return render(request, 'loginapp/Html file/SignIn.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homePage(request):
    context = {}
    return render(request, 'loginapp/Html file/Home.html', context)

# class Blog(ListView):
#     model = Post
#     template_name = 'home.html'