from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    Occupants_Count = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    police_dept = models.IntegerField(default='999')
    health_dept = models.IntegerField(default='0700003434')



    def __str__(self):
        return self.name


    @classmethod
    def get_neighbourhoods(cls):
        neighbourhood = Neighbourhood.objects.all()
        return neighbourhoods

    @classmethod
    def find_neighbourhood_by_id(cls,id):
        neighbourhood = Neighbourhood.objects.get(id=id)
        return neighbourhood

    @classmethod
    def search_by_neighbourhood(cls,name):
        neighbourhood = Neighbourhood.objects.filter(user__username__icontains=name)
        return neighbourhood

class Profile(models.Model):
    name = models.CharField(max_length = 30)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    hood = models.OneToOneField(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

