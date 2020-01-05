from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['first_name']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            #Check username:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken.')
                return redirect('accounts:register')
            # Check email:
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used.')
                return redirect('accounts:register')
            else:
                #looks good
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                messages.success(request, 'You are now registered and can log in')
                return redirect('accounts:login')



        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('accounts:register')


    else:
        return render(request, "accounts/register.html")


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/login.html")
