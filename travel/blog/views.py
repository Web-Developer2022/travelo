from django.shortcuts import render
from django.views import View
from locals import lang_pack
from django.http import JsonResponse
from .models import *
# Create your views here.


class HomeView(View):
    def get(self,request):
        directions = Destinations.objects.all()
        context = {
            "directions":directions
        }
        return render(request , "index.html"  , context)



def change_lang( request):
    lang = request.GET.get("current_lang")
    request.session["lang"] = lang
    return JsonResponse({"status":200})
    