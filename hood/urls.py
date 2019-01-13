from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^new/profile$',views.add_profile,name='add_profile'),
    url(r'searched/', views.search_results, name='search_results'),
    url(r'^home/$',views.home,name = 'home'),
    url(r'^new/business$', views.new_business, name='new_business'),
    url(r'^new/hood$', views.new_hood,name= 'new_hood'),
    url(r'^update_profile/$',views.update_profile,name= 'update_profile'),




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)