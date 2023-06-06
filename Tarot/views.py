from django.shortcuts import render
import calendar
from django.views import View
from django.views.static import serve

# Create your views here.


class TarotView(View):
    def get(self, request):
        return render(request, "HomePage.html")

    def serve_static_file(request):
        response = serve(request, "css/styles.css")

        response["Cache-Control"] = "no-cache, no-store, must-revalidate"
        return response

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


# def getdate (request){
# if request.method == 'POST':
#     current_year= calendar.datetime.datetime.now().year
#     return render(request, "Calendar.html", {'current_year':current_year})
# }
