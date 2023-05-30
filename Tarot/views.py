from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.static import serve
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class LoginPageView(View):
    def get(self, request):
        return render(request, 'login_page.html')
    def post(self ,request ):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print(user_name, password)
        check_login = authenticate(username= user_name, password = password)
        if check_login is None :
            return render(request, 'login_page.html', {'error': 'Tên đăng nhập hoặc mật khẩu không đúng'})
        login(request, check_login)
        return render(request, 'HomePage.html')
class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'home_page.html')
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/login/')