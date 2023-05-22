from django.shortcuts import render
from django.views import View
from django.views.static import serve

# Create your views here.


class TarotView(View):
    def get(self, request):
        return render(request, 'HomePage.html')
    def serve_static_file(request):
        response = serve(request, 'css/styles.css')
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response