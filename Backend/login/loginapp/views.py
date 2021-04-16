from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse, reverse_lazy


from django.contrib.auth import authenticate, login, logout 
from .models import Post
from .forms import CreateUserForm, PostForm ,EditForm

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView


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
        return redirect('home')
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
    return render(request, 'loginapp/Html file/index.html', context)

class Blog(ListView):
    model = Post
    template_name = 'loginapp/Html file/blog.html'

class Detail_Article_View(DetailView):
    model = Post
    template_name = 'loginapp/Html file/detailed_article.html'

class AddPostView(LoginRequiredMixin,CreateView, ListView):
    model = Post
    form_class = PostForm
    template_name = 'loginapp/Html file/Dashboard.html'
    success_url = reverse_lazy('dashboard')
    # fields = '__all__'

class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'loginapp/Html file/edit.html'
    # fields = ['title','auth' ,'body','category']
    success_url = reverse_lazy('dashboard')
    def from_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)

class  DeletePostView(DeleteView,LoginRequiredMixin):
    model = Post
    template_name = 'loginapp/Html file/Delete.html'
    success_url = reverse_lazy('dashboard')
    def from_valid (self,form) :
        form.instance.auth = self.request.user
        return super().form_valid(form)




