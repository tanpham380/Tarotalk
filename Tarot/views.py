
from django.shortcuts import render
import calendar
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from Tarot.models import User
from .forms import RegisterForm
import random

# Create your views here.



def chatbot(request):
    return render(request, "Chatbox.html")

def listReader(request):
    return render(request, "ListReader.html")

def profile(request):
    return render(request, "profile.html")

def question(request):
    return render(request, "Questions.html")

def package(request):
    return render(request, "Package.html")

def hour(request):
    return render(request, "Hour.html")

def chooseSlot(request):
    return render(request, "ChooseSlot.html")

def checkout(request):
    return render(request, "CheckOut.html")

def calendar(request):
    return render(request, "Calendar.html")

class LoginPageView(View):
    def get(self, request):
        return render(request, "HomePage.html")
    def post(self, request):
        user_name = request.POST.get('email')
        password = request.POST.get('password')
        print(user_name, password)
        check_login = authenticate(username=user_name, password=password)
        if check_login is None:
            return render(request, 'login_page.html', {'error': 'Tên đăng nhập hoặc mật khẩu không đúng'})
        login(request, check_login)
        return render(request, 'homepage.html')


class ViewUser( View):
    login_url = '/login/'
    def get(self, request):
        istarot_users = User.objects.filter(istarot=True)
        random_users = random.sample(list(istarot_users), 4)
        context = {'istarot_users': random_users}
        return render(request, 'homepage.html', context)

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register_page.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=email):
                form.add_error('email', 'Tên đăng nhập đã tồn tại')
                return render(request, 'register_page.html', {'form': form})
            user = form.save(commit=False)
            user.username = email.lower()
            user.save()
            password = form.cleaned_data.get('password1')  # Get the password from cleaned_data
            check_login = authenticate(username=user.username, password=password)
            if check_login is not None:
                login(request, check_login)
                return render(request, 'register_sucessfully.html')
            else:
                # Handle authentication error
                # Example: display error message to the user
                form.add_error(None, 'Lỗi xác thực người dùng')
                return render(request, 'register_page.html', {'form': form})
        else:
            return render(request, 'register_page.html', {'form': form})


class TestPageView(View) :
    def get(self, request):
        return render(request, 'register_sucessfully.html')


    
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/login/')
