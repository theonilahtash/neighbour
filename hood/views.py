from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Neighbourhood,Business
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
    neighbourhoods = Neighbourhood.objects.all()
    businesses = Business.objects.all()
    return render(request, 'index.html',{"neighbourhoods":neighbourhood,"businesses":businesses})

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

@login_required(login_url='/accounts/login/')
def new_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit = false)
            business.user = current_user
            business.save()
            return redirect('search_results')

    else:
        form = BusinessForm()
        return render(request,'business.html')
