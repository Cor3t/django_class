from django.shortcuts import render, redirect
from store1.forms import CreatePostFrom, RegisterForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'html/home.html')

def createpost(request):
    if request.method == 'POST':
        form = CreatePostFrom(request.POST)
        if form.is_valid():
            form.save(commit=False)
            
    else:
        form = CreatePostFrom()
    return render(request, 'html/createpost.html', {'form':form, 'title': 'Create a post'})

def auth_login(request):
    if request.method == 'POST':
        user = request.POST.get('uname')
        password =request.POST.get('password')
        user = authenticate(username = user, password= password)
        if user:
            return redirect('/')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})