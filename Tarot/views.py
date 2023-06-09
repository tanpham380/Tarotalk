
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
from django.urls import reverse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from datetime import date



# Create your views here.



def chatbot(request):
    return render(request, "Chatbox.html")

def listReader(request):
    return render(request, "ListReader.html")

# class profileUser(View):
#     def get(request):
#         return render(request, "Profile.html")
class profileuser(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'profile.html', {'User': user })
    # def post(self,request, user_id):
    #     if 'xem_theo_gio' in request.POST:
    #         user = User.objects.get(user_id)

    #         return render  (request, 'Hour.html', {'User': user })
    #     elif 'xem_theo_so_luong_cau_hoi' in request.POST:
    #         user = User.objects.get(id=user_id)
    #         return render  (request, 'Questions.html', {'User': user })
    #     elif 'xem_theo_goi' in request.POST:
    #         user = User.objects.get(id=user_id)
    #         return render  (request, 'Package.html', {'User': user })
        
        
        
        
# def question(request):
#     return render(request, "Questions.html")
class question(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'Questions.html', {'User': user })
# def package(request):
#     return render(request, "Package.html")
class package(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'Package.html', {'User': user })
# def hour(request):
#     return render(request, "Hour.html")
class hour(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'Hour.html', {'User': user })
def chooseSlot(request):
    return render(request, "ChooseSlot.html")

class checkout(LoginRequiredMixin,View ):
    login_url = '/login/'
    def get(self, request):
        return render(request, "CheckOut.html")

# def calendar(request):
#     return render(request, "Calendar.html")
class calendar(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'Calendar.html', {'User': user })

# def user_detail(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     # Đảm bảo rằng bạn truyền đúng tên trường hoặc thuộc tính để truy xuất thông tin của người dùng

#     return render(request, 'user_detail.html', {'user': user})

class LoginPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('Tarot:HomePage')
        return render(request, 'login_page.html')
    
    def post(self, request):
        user_name = request.POST.get('email')
        password = request.POST.get('password')
        print(user_name, password)
        check_login = authenticate(username=user_name, password=password)
        if check_login is None:
            return render(request, 'login_page.html', {'error': 'Tên đăng nhập hoặc mật khẩu không đúng'})
        login(request, check_login)
        #homepage_url = reverse('HomePage')
        return redirect('Tarot:HomePage')


class ViewUser(View):
    login_url = '/login/'
    def get(self, request):
        istarot_users = User.objects.filter(istarot=True)
        random_users = random.sample(list(istarot_users), min(5, istarot_users.count()))
        context = {'istarot_users': random_users}
        return render(request, 'HomePage.html', context)

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
        return render(request, 'Post.html')

class PostView(View) :
    def get(self, request):
        return render(request, 'Post.html')    
class EventView(View) :
    def get (self, request):
        return render(request, 'Event.html')
    
       
class Account(View) :
    def get(self, request):
        isReader= request.user

        if request.user.is_authenticated and isReader.istarot:
            user = User.objects.get(id=request.user.id)
            return render(request, 'ReaderAccount.html', {'User': user })
        if request.user.is_authenticated :
            user = User.objects.get(id=request.user.id)
            return render(request, 'UpgradeAccount.html', {'User': user })
        
        return render(request, 'Account.html')
        
    def post(self, request):
        if 'avatar' in request.FILES:
            if request.FILES['avatar'] is None:
                return redirect('Tarot:HomePage')
            else:
                picture = request.FILES['avatar']
                user = User.objects.get(id=request.user.id)
                old_avatar = user.avatar
                default_storage.delete(old_avatar.path)
                username = user.id
                today = date.today()
                filename = f"id_{username}_{today}.{picture.name.split('.')[-1]}"
                user.avatar.save(filename, picture)
                user.save()
                return redirect('Tarot:account')

                
        
class GuideView(View) :
    def get(self, request):
        return render(request, 'Guide.html')        
class PaidSuccessfullyView(View):
    def get(self, request):
        return render(request, 'PaidSuccessfully.html')
class MoreReaderView(View):
    def get(self, request):
        istarot_users = User.objects.filter(istarot=True)
        return render(request, 'more_reader.html', {'istarot_users': istarot_users })


class UpdateUserView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        form = UpgradeUserForm()
        return render(request, 'upgrade_User.html', {'form': form})
    
    def post(self, request):
        form = UpgradeUserForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = request.user
            picture = form.cleaned_data.get('avatar')
            old_avatar = user.avatar
            if old_avatar:
                default_storage.delete(old_avatar.path)
            username = user.id
            today = date.today()
            filenameavatar = f"id_{username}_{today}.{picture.name.split('.')[-1]}"
            user.avatar.save(filenameavatar, picture)
            coverpage = form.cleaned_data.get('cover_page')
            old_coverpage = user.cover_page
            if old_coverpage:
                default_storage.delete(old_coverpage.path)
            filenammecoverpage= f"id_{username}_{today}.{coverpage.name.split('.')[-1]}"
            user.cover_page.save(filenammecoverpage, coverpage)
            user.introduction = form.cleaned_data.get('introduction')
            user.status = form.cleaned_data.get('status')
            user.save()
            
            return render(request, 'update_user_succesfull.html')
        else:
            print(form.errors)
            return render(request, 'upgrade_User.html', {'form': form})


        
        
def xinloipagenaychuahoatdong(request):
    return render(request, 'xinloi.html')
    
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/login/')