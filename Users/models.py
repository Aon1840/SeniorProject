from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15,unique=True,blank=False)
    password = models.CharField(max_length=20,blank=False)
    name = models.CharField(max_length=30,blank=False)
    surname = models.CharField(max_length=30,blank=False)
    tel = models.CharField(max_length=10,blank=False)
    email = models.EmailField(max_length=50,unique=True,blank=False)
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('user_id',)
