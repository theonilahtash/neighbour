from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Neighbourhood,Business
from .forms import NewProfileForm,NewBusinessForm

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    neighbourhoods = Neighbourhood.objects.all()
    businesses = Business.objects.all()
    return render(request, 'index.html',{"neighbourhoods":neighbourhoods,"businesses":businesses})

@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    profiles = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request,'profile.html',{"profiles":profiles})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')
    else:
        form = NewProfileForm()
    return render(request,'new_profile.html', {"form":form})



def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "Searched"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_business(request):
    if request.method == 'POST':
        form = NewBusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit = false)
            business.user = current_user
            business.save()
            return redirect('welcome')

    else:
        form = NewBusinessForm()
        return render(request,'new_business.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    if request.method =='POST':
        form = NewHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=false)
            hood.user = current_user
            hood.save()
            return redirect('welcome')
    else:
        form = NewHoodForm()
        return render(request,'new_hood.html',{"form":form})
