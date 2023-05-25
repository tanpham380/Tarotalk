from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='static/avatars/', null=True, blank=True)
    cover_page = models.ImageField(upload_to='static/cover_pages/', null=True, blank=True)
    name = models.CharField(max_length=255,  )
    tarot_role = models.CharField(max_length=50, default= "Tarot Reading and AStrology")
    introduction = models.TextField()
    status = models.CharField(max_length=255)
    start_vote = models.IntegerField()
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,  )
    groups = models.ManyToManyField(Group, related_name='tarot_users')
    user_permissions = models.ManyToManyField(Permission, related_name='tarot_users')
class dich_vu (models.Model ):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255,  )
    price = models.IntegerField()
    content = models.TextField()
    date  = models.DateField()
    