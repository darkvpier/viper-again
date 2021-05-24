from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User
from .forms import StudentSignUpForm, CoordinatorSignUpForm

def register(request):
    return render(request, 'accounts/index.html')

"""
class StudentRegister(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/student_register.html'

    def validate(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
"""

def StudentRegister(request):
    form = StudentSignUpForm()
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    return render(request, 'accounts/student_register.html', {'form':form})


def CoordinatorRegister(request):
    form = CoordinatorSignUpForm()
    if request.method == "POST":
        form = CoordinatorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    return render(request, 'accounts/coordinator-register.html', {'form':form})


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request, user)
                if user.is_student:
                    return redirect('core:student-dashboard')
                   #return HttpResponse("Student view")
                elif user.is_coordinator:
                    return redirect('core:coordinator-dashboard')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
