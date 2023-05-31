from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from Tarot.models import User
from .forms import RegisterForm

# Create your views here.


class LoginPageView(View):
    def get(self, request):
        return render(request, 'login_page.html')
    
    def post(self, request):
        user_name = request.POST.get('email')
        password = request.POST.get('password')
        print(user_name, password)
        check_login = authenticate(username=user_name, password=password)
        if check_login is None:
            return render(request, 'login_page.html', {'error': 'Tên đăng nhập hoặc mật khẩu không đúng'})
        login(request, check_login)
        return render(request, 'homepage.html')


class ViewUser(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'homepage.html')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register_page.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=email).exists():
                form.add_error('email', 'Tên đăng nhập đã tồn tại')
                return render(request, 'register_page.html', {'form': form})
            user = form.save(commit=False)
            user.username = email.lower()
            user.save()
            check_login = authenticate(username=user.username, password=user.password)
            login(request, check_login)
            return render(request, 'register_sucessfully.html')
        else:
            return render(request, 'register_page.html', {'form': form})




    
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/login/')