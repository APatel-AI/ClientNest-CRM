from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 

#toast messages
from django.contrib import messages

from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()


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
        return render(request, 'home.html', {'records':records})


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


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "Login or Register to view the records")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_client = Record.objects.get(id=pk)
        delete_client.delete()
        messages.success(request, "Client Has Been Removed From ClientNest!")
        return redirect('home' )
    else:
        messages.success(request, "Login or Register to delete the record")
        return redirect('home' )

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Client has been added!")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Please Login/Register To Add Client")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        #instance... have a filled out form that need to be updated
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Client Information Has Been Updated")
            redirect('home')
        return render(request, 'update_record.html', {'form':form})

    else:   
        messages.success(request, "Please Login/Register To Update Client Information")
        return redirect('home')






