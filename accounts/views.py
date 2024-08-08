from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')