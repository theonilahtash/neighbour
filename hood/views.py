from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .models import Profile,Neighbourhood,Business
from .forms import NewProfileForm,NewBusinessForm,NewHoodForm,UpdateProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    neighbourhoods = Neighbourhood.objects.all()
    businesses = Business.objects.all()
    return render(request, 'index.html',{"neighbourhoods":neighbourhoods,"businesses":businesses})

@login_required(login_url='/accounts/login/')
def profile(request):

	profile = Profile.objects.get(user = request.user)
  
	return render(request,'profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
	profile = Profile.objects.get(user = request.user)
	if request.method == 'POST':
		form = UpdateProfileForm(request.POST,instance = profile )
		if form.is_valid():
			form.save()
			messages.success(request, 'Successful profile edit!')
			return redirect('profile')
	else:
		form = UpdateProfileForm(instance = profile )
		return render(request,'update_profile.html',{"profile":profile})


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

def home(request):
  neighbourhoods = Neighbourhood.objects.filter(user=request.user)
  return render(request,'home.html',{"neighbourhoods":neighbourhoods})



def search_results(request):
    if 'neighbourhoods' in request.GET and request.GET["neighbourhoods"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbourhoods = Neighbourhood.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"neighbourhoods": searched_neighbourhoods})

    else:
        message = "Searched"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_business(request):
    if request.method == 'POST':
        form = NewBusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit = False)
            business.user = current_user
            business.save()
            return redirect('welcome')

    else:
        form = NewBusinessForm()
        return render(request,'new_business.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    if request.method =='POST':
        # neighbourhoods = Neighbourhood.objects.filter(user=request.user)
        form = NewHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit = False)
            # hood.user = request_user
            hood.save()
            return redirect('welcome')
    else:
        form = NewHoodForm()
        return render(request,'new_hood.html',{"form":form})
