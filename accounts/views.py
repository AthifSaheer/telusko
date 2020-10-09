from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2: #password matching cheking
            if User.objects.filter(username=user_name).exist(): #username already taken cheking
                messages.info(request, 'username already taken')
                return redirect('register')
                #print("Username alrady taken")
            elif User.objects.filter(email=email).exist():
                messages.info(request, 'username email taken')
                return redirect('register')
                #print("Emial already taken")
            else:
                user = User.objects.create_user(user_name=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print("User Created")
        else:
            messages.info(request, 'username password taken')
            return redirect('register')
            #print("password not matching....")
        return redirect('/')
    else:    
        return render(request, 'register.html')
