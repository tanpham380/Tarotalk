from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    name = models.CharField(max_length=255,  )
    tarot_role = models.CharField(max_length=255, default= "Tarot Reading and AStrology")
    status = models.CharField(max_length=255, default= "Active")
    start_vote = models.IntegerField(default=0,  MaxValueValidator = 5, MinValueValidator = 0)
    birth_date = models.DateField()
    groups = models.ManyToManyField(Group, related_name='tarot_users')
    user_permissions = models.ManyToManyField(Permission, related_name='tarot_users')
    