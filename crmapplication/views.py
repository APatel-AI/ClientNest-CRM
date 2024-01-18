from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 

#toast messages
from django.contrib import messages

from .forms import SignUpForm

def home(request):
    #logging in check
    if request.method == 'POST':
        #action if post request
        #double check name given to form
        username = request.POST['username']
        password = request.POST['password']
        #AUTHENTICATE
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In !")
            return redirect('home')
        else:
            messages.success(request, "Error Logging In Please Try Again!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


#frontend login feature
#def login_user(request):
   # pass

#frontend logout feature
def logout_user(request):
   logout(request)
   messages.success(request, "You have been logged out!")
   return redirect ('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and log user in if form is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcom to ClientNest")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})