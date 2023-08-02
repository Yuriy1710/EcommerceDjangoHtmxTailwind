from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from product.models import *
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()           
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})


@login_required
def my_account(request):
    return render(request, 'my-account.html')

@login_required
def edit_my_account(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        
        return redirect('my_account')   
    return render(request, 'edit-my-account.html')


def frontpage(request):
    products = Product.objects.all()[0:8]
    context = {'products': products}
    return render(request, 'frontpage.html', context)


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)
        
    query = request.GET.get('query', '')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'products': products, 
        'categories': categories,
        'active_category': active_category
        }
    return render(request, 'shop.html', context)
