from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserCreationForm, UserLoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def create_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/success.html')
    
    context = {
        'form':form
    }
    return render(request, 'users/create_user.html', context)

def login_user(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponse('Login sucessfull')
            else:
                form.add_error(None, 'invalid usernme or pswd')

    context = {
        'form':form
    }

    return render(request, 'users/login_user.html', context)

def logout_user(request):
    logout(request)
    return HttpResponse('loggedout')