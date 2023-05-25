from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    name = models.CharField(max_length=255,  )
    groups = models.ManyToManyField(Group, related_name='tarot_users')
    user_permissions = models.ManyToManyField(Permission, related_name='tarot_users')
    