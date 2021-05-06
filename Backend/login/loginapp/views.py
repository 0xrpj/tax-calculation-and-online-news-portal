from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


from django.contrib.auth import authenticate, login, logout
from .models import Post, Tax
from .forms import CreateUserForm, PostForm, EditForm, TaxCalculation

from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Dispaly for register page


def registerPage(request):
    # Checks login status and if loggedin redirects to home page
    if request.user.is_authenticated:
        return redirect('home')
    # Checks login status and if not loggedin execute following
    else:
        # Fetches values from CreateUserForm fields
        form = CreateUserForm()
        # Checks the form method='POST' inside Register.html
        if request.method == 'POST':
            # sends post request to CreateUserForm
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # user = form.cleaned_data.get('username')
                # messages.success(request, 'Account was created for '+user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'loginapp/Html file/Register.html', context)


def loginPage(request):
    # Checks login status and if loggedin redirects to home page
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            # fetches username and password from user input
            username = request.POST.get('username')
            password = request.POST.get('password')
            # checks the fetched data with the user database data
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Email OR password is incorrect')
                return redirect('login')
        context = {}
        return render(request, 'loginapp/Html file/SignIn.html', context)


# requests for logout then redirects to SignIn.html
def logoutUser(request):
    logout(request)
    return redirect('login')

# If user is not logged in it redirects


def loginPageRedirect(request):
    return redirect('login')

# @login_required(login_url='login')
# def homePage(request):
#     context = {}
#     return render(request, 'loginapp/Html file/index.html', context)


# Views through classes

# For detail article page
class Detail_Article_View(DetailView):
    model = Post
    # location to make post model visible
    template_name = 'loginapp/Html file/blog.html'

# For detail home page


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    # location to make post model visible
    template_name = 'loginapp/Html file/index.html'


class PoliticsView(LoginRequiredMixin, ListView):
    model = Post
    # location to make post model visible
    template_name = 'loginapp/Html file/Politics.html'


class EntertainmentView(LoginRequiredMixin, ListView):
    model = Post
    # location to make post model visible
    template_name = 'loginapp/Html file/Entertainment.html'


class SportsView(LoginRequiredMixin, ListView):
    model = Post
    # location to make post model visible
    template_name = 'loginapp/Html file/Sports.html'


class BusinessView(LoginRequiredMixin, ListView):
    model = Post
    # location to make post model visible
    template_name = 'loginapp/Html file/Business.html'


# For dashboard page
class AddPostView(LoginRequiredMixin, CreateView, ListView):
    model = Post
    form_class = PostForm
    # location to make post model visible
    template_name = 'loginapp/Html file/Dashboard.html'
    # if delete is success redirect to dashboard
    success_url = reverse_lazy('dashboard')

    # fields = '__all__'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    # location to make post model visible
    template_name = 'loginapp/Html file/edit.html'

    # fields = ['title','auth' ,'body','category','header_image']

    # if delete is success redirect to dashboard
    success_url = reverse_lazy('dashboard')

    def from_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)


class DeletePostView(DeleteView, LoginRequiredMixin):
    model = Post
    # location to make post model visible
    template_name = 'loginapp/Html file/Delete.html'
    # if delete is success redirect to dashboard
    success_url = reverse_lazy('dashboard')

    def from_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)


def Tax_calculator(request):
    if request.method == 'POST':
        Tax = Tax.objects.get()
        Tax.blur_quantity = request.POST['annual_gross_salary']
        Tax.save()
    template_name = 'loginapp/Html file/taxCalculator'
    success_url = reverse_lazy('home')
    return render(request, 'loginapp/Html file/TaxCalculator.html')


def Tax_History(request):
    all_members = Tax.objects.all
    return render(request, 'loginapp/Html file/TaxHistory.html', {'all':all_members })


def AboutView(request):
    model = Post
    return render(request, 'loginapp/Html file/About.html')