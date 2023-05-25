from django.shortcuts import render
from django.views import View
from django.views.static import serve

# Create your views here.


class TarotView(View):
    def get(self, request):
        return render(request, 'register_page.html')
