from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class userverify(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_verified=models.BooleanField(default=False)
    otp=models.IntegerField()

    def __str__(self):
        return self.user.username



class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=120)
    category=models.CharField(max_length=120,default="")
    price=models.IntegerField()
    image=models.ImageField(upload_to="product")
    desc=models.CharField(max_length=1500)

    def __str__(self) -> str:
        return f"{self.category}"