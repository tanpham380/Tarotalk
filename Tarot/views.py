from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm
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
        return render(request, 'homepage.html')

class ViewUser(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'homepage.html')
    
class RegisterView(View):
    template_name = 'register_page.html'
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomePage')  # Replace 'home' with the name of your home page URL pattern
        return render(request, self.template_name, {'form': form})
    
    
    
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/login/')