from django.db import models
from Users.models import User

# Create your models here.
class CarPosition(models.Model):
    carPosition_id = models.AutoField(primary_key=True)
    position_id = models.CharField(max_length=3,blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_driveOut = models.BooleanField(initial=False,blank=False)
    time_created = models.Date(auto_now_add=True)

    class Meta:
        ordering = ('carPosition_id',)