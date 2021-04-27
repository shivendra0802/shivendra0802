from django.shortcuts import render, redirect
# from .forms import LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def base(request):
    return render(request, 'order/base.html')

# @login_required(login_url='login')
def home(request):
    return render(request, 'order/home.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')         
    else: 
        form = LoginForm(request.GET)
    return render(request, 'order/login.html', {'form': form})



def staff_login(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
    else:
        form = AdminForm(request.GET)
    return render(request, 'order/stafflogin.html', {'form': form})
        




def user_register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            return redirect('login')
    else:
        form = SignupForm()        
    return render(request, 'order/register.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    sp = Product.objects.all()
    return render(request, 'order/dashboard.html',  {'sp': sp})



def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def add_to_cart(request):
    return render(request, 'order/cart.html')

@login_required(login_url='login')
def show_product(request, id):
    cat = Product.objects.get(id=id)
    sp = Product.objects.all()
    return render(request, 'order/show_pro.html', {'sp': sp, 'cat': cat})

@login_required(login_url='login')
def buy_now(request):
    return render(request, 'order/buy_now.html') 

@login_required(login_url='login')
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    print(cart)
    amount = 0.0
    shipping_amount = 100.0
    totalamount = 0.0
    if cart:
        for p in cart:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
            totalamount = amount + shipping_amount
            # {'cart': cart, 'totalamount': totalamount, 'amount': amount, 'shipping_amount': shipping_amount}
    return render(request, 'order/show_cart.html', {'cart': cart, 'totalamount': totalamount, 'amount': amount, 'shipping_amount': shipping_amount})  


def up_dash(request):
    if request.method == 'POST':
        # user = request.user
        form = UpDashForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = UpDashForm()
    return render(request, 'order/dash.html', {'form': form})         

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('dash')
    else:
        form = CategoryForm()
    return render(request, 'order/addcategory.html', {'form': form})            

 
def delete_category(request, id):
    Category.objects.get(id=id).delete()
    return redirect('addcategory')





