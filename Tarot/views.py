
from django.shortcuts import render
import calendar
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from Tarot.models import User
from .forms import *
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
# def user_detail(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     # Đảm bảo rằng bạn truyền đúng tên trường hoặc thuộc tính để truy xuất thông tin của người dùng

#     return render(request, 'user_detail.html', {'user': user})

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


class ViewUser(LoginRequiredMixin ,View):
    login_url = '/login/'
    def get(self, request):
        istarot_users = User.objects.filter(istarot=True)
        random_users = random.sample(list(istarot_users), 5)
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


class TestPageView(LoginRequiredMixin,View) :
    login_url = '/login/'
    def get(self, request):
        form = UpgradeUserForm()
        return render(request, 'upgrade_User.html', {'form': form})
    def post(self, request):
        form = UpgradeUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.introduction = form.cleaned_data.get('introduction')
            user.status = form.cleaned_data.get('status')
            user.cover_page = form.cleaned_data.get('cover_page')
            user.avatar = form.cleaned_data.get('avatar')
            user.save()
            return render(request, 'update_user_succesfull.html')
        else:
            return render(request, 'upgrade_User.html', {'form': form})
    
        

class MoreReaderView(View):
    def get(self, request):
        istarot_users = User.objects.filter(istarot=True)
        return render(request, 'more_reader.html', {'istarot_users': istarot_users })





# views.py
from django.shortcuts import render, redirect


def create_post(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        # Tạo bài viết mới với user_id
        # Thực hiện kiểm tra và lưu bài viết
        
        # Chuyển hướng trở lại trang ban đầu hoặc trang thành công
        return redirect('home')  # Chỉnh sửa tên của URL nếu cần thiết
    
    return redirect('home')  # Xử lý yêu cầu GET hoặc yêu cầu không hợp lệ

    
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/login/')