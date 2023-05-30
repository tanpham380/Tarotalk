from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='static/avatars/', null=True, blank=True)
    cover_page = models.ImageField(upload_to='static/cover_pages/', null=True, blank=True)
    tarot_role = models.CharField(max_length=50, default= "Tarot Reading and AStrology")
    introduction = models.TextField(null=True)
    status = models.CharField(max_length=255, null=True)
    start_vote = models.IntegerField(null=True)
    birth_date = models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=10,null=True  )
class dich_vu (models.Model ):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255,  )
    price = models.IntegerField()
    content = models.TextField()
    date  = models.DateField()
    