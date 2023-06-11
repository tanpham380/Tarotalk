
from django.shortcuts import render
import calendar
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from Tarot.models import *
from .forms import *
import random
from django.urls import reverse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from datetime import date
from datetime import datetime
from django.utils import timezone


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
class chooseSlot(View):
    def get (self, request):
        return render(request, "ChooseSlot.html")
    def post (self, request):
        pass
import locale
import collections

from collections import Counter
from django.contrib import messages


class checkout(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        list_dich_vu = giao_dich.objects.filter(user_id=user,user_use = request.user, is_paid = False, is_delete = False)
        total = 0
        giao_dich_counts = Counter()
        
        for item in list_dich_vu:
            total += item.price
            giao_dich_counts[item.name] += 1
        
        locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
        total_vnd = locale.format_string("%d", total, grouping=True) + " VNĐ"
       
        giao_dich_items = giao_dich_counts.items()
        return render(request, 'CheckOut.html', {'User': user, 'list_dich_vu': list(giao_dich_items), 'total': total_vnd })
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        item_value = request.POST.get('item')
        list_dich_vu = giao_dich.objects.filter(user_id=user,user_use = request.user, is_paid = False, is_delete = False)
        a = request.POST
        for item in list_dich_vu : 
            if item_value == item.name:
                item.is_delete = True
                item.save()
                
        list_dich_vu = giao_dich.objects.filter(user_id=user,user_use = request.user, is_paid = False, is_delete = False)
        total = 0
        giao_dich_counts = Counter()        
        for item in list_dich_vu:
            total += item.price
            giao_dich_counts[item.name] += 1
        locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
        total_vnd = locale.format_string("%d", total, grouping=True) + " VNĐ"
        giao_dich_items = giao_dich_counts.items()
        return render(request, 'CheckOut.html', {'User': user, 'list_dich_vu': list(giao_dich_items), 'total': total_vnd })
# def calendar(request):
#     return render(request, "Calendar.html")
class calendar(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'Calendar.html', {'User': user })
    def post(self, request, user_id):
        current_date = timezone.now()
        user = User.objects.get(id=user_id)
        user_use= request.user
        if '30phut' in request.POST:
            # User selected 30phut, so save it in the dich_vu table
            dich_vu_obj = giao_dich.objects.create(is_paid = False ,user_id=user, name='30 phút - 1 chủ đề - 80.000 đồng', price=80000, date=current_date , user_use=user_use)
            dich_vu_obj.save()
        else: print("Không có 30 phút")
        if '60phut' in request.POST:
            # User selected 60phut, so save it in the dich_vu table
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='60 phút - 1 chủ đề - 150.000 đồng', price=150000, date=current_date , user_use=user_use)
            dich_vu_obj.save()
        if 'tongquan' in request.POST:
            # User selected tongquan, so save it in the dich_vu table
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='Trải bài tổng quan - 250.000 đồng', price=250000, date=current_date, user_use=user_use)
            dich_vu_obj.save()
        if 'tinhduyen' in request.POST:
            # User selected tinhduyen, so save it in the dich_vu table
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='Trải bài tình duyên - 200.000 đồng', price=200000, date=current_date, user_use=user_use)
            dich_vu_obj.save()
        if 'giadinh' in request.POST:
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='Trải bài gia đình - 180.000 đồng', price=180000, date=current_date, user_use=user_use)
            dich_vu_obj.save()
        if 'hoctap' in request.POST:
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='Trải bài về học tập - 180.000 đồng', price=180000, date=current_date, user_use=user_use)
            dich_vu_obj.save()
        if 'congviec' in request.POST:
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='Trải bài về công việc - 180.000 đồng', price=180000, date=current_date, user_use=user_use)
            dich_vu_obj.save()       
        if 'quanhe' in request.POST:
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='Trải bài mối quan hệ - 200.000 đồng', price=200000, date=current_date, user_use=user_use)
            dich_vu_obj.save()    
        if '3cauhoi' in request.POST:
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='3 câu hỏi - 100.000 đồng', price=100000, date=current_date, user_use=user_use)
            dich_vu_obj.save()
        if '6cauhoi' in request.POST:
            dich_vu_obj = giao_dich.objects.create(is_paid = False,user_id=user, name='5 câu hỏi - 120.000 đồng', price=120000, date=current_date, user_use=user_use)
            dich_vu_obj.save()                                                
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