from django.db.models import fields
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


from django.contrib.auth import authenticate, login, logout
from .models import History, Post, Tax, TaxOne
from .forms import CreateUserForm, PostForm, EditForm, TaxCalculation

from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def search(request):
    if request.method == 'GET':
        searched = request.GET['search']
        filtered = Post.objects.filter(title__contains=searched)
        posts = Post.objects.all()

        context = {'searched': searched,
        'filtered': filtered, 'posts': posts}
        return render(request, "loginapp/Html file/search.html",context)


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

            def isNum(data):
                try:
                    # data == 'akash'
                    int(data)
                    return True
                except ValueError:
                    return False    


            # def clean_username(self):
            #     username_passed = self.cleaned_data.get('username')
                

            if form.is_valid():
                username = form.cleaned_data.get('username')
                if isNum(username):
                    # try:    
                    #     raise forms.ValidationError("Invalid username can't be only numbers.")
                    # except:
                    messages.info(request, 'Invalid username, can not be only numbers.')   
                else:
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

    def get_context_data(self, *args, **kwargs):
        context = super(Detail_Article_View, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.all()
        return context


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
        monthly_salary = request.POST['monthly_salary']
        no_months = request.POST['no_months']
        bonus = request.POST['bonus']
        allowance = request.POST['allowance']
        emp_provident = request.POST['emp_provident']
        CIT = request.POST['CIT']
        insurance = request.POST['insurance']
        annual_gross_salary = float(monthly_salary)*float(no_months)
        taxable_income = float(annual_gross_salary) + float(bonus) + \
            float(allowance) - float(emp_provident) - \
            float(CIT) - float(insurance)
        if(taxable_income <= 400000):
            tax_slab_percentage = '1%'
            net_payable_tax = taxable_income * 0.01

        elif(taxable_income > 400000) and (taxable_income <= 500000):
            tax_slab_percentage = '10 %'
            net_payable_tax = 0.01*400000 + 0.10 * (taxable_income-400000)

        elif (taxable_income > 500000) and (taxable_income <= 700000):
            tax_slab_percentage = '20 %'
            net_payable_tax = 0.01*400000 + 0.10 * \
                100000 + 0.20 * (taxable_income-500000)

        elif(taxable_income > 700000 and taxable_income <= 2000000):
            tax_slab_percentage = '30 %'
            net_payable_tax = 0.01*400000 + 0.10 * 100000 + \
                0.20 * 200000 + 0.30 * (taxable_income-700000)
        elif(taxable_income > 2000000):
            tax_slab_percentage = '36 %'
            net_payable_tax = 0.01*400000 + 0.10 * 100000 + 0.20 * \
                200000 + 0.30 * 1300000 + 0.36 * (taxable_income-2000000)
        else:
            tax_slab_percentage = 'weird error'
            net_payable_tax = 0
        # str(taxable_income).save()
        print("Annual Gross Salary: " + str(annual_gross_salary))
        print("Slab percentage: " + str(tax_slab_percentage))
        print("Taxable income: " + str(taxable_income))
        print("Net payable tax: " + str(net_payable_tax))

        # db_name = Tax(monthly_salary=monthly_salary, no_months=no_months, bonus=bonus,
        #               allowance=allowance, emp_provident=emp_provident, CIT=CIT, insurance=insurance)
        db_name = TaxOne(annual_gross_salary=annual_gross_salary, tax_slab_percentage=tax_slab_percentage,
                         taxable_income=taxable_income, net_payable_tax=net_payable_tax)
        db_name.save()
        # annual_gross_salary = request.POST['annual_gross_salary']
        # tax_slab_percentage = request.POST['tax_slab_percentage']
        # net_payable_tax = request.POST['net_payable_tax']
    return render(request, 'loginapp/Html file/TaxCalculator.html')


def Tax_History(request):
    all_members = History.objects.all
    return render(request, 'loginapp/Html file/TaxHistory.html', {'all': all_members})


def AboutView(request):
    model = Post
    return render(request, 'loginapp/Html file/About.html')
