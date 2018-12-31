from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 30)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    hood = models.OneToOneField(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

