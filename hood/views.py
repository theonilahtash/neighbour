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