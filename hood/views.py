from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Neighbourhood
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    profiles = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request,'profile.html',{"profiles":profiles})

def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "Searched"
        return render(request, 'search.html',{"message":message})
