from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True , default='avatars/default_avatar.png')
    cover_page = models.ImageField(upload_to='cover_pages/', null=True, blank=True , default='cover_pages/banner.png')
    tarot_role = models.CharField(max_length=50, default= "Tarot Reading and AStrology")
    introduction = models.TextField(null=True)
    status = models.CharField(max_length=255, null=True)
    star_vote = models.IntegerField(null=True,default= 0)
    birth_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=10,null=True)
    istarot = models.BooleanField(default=False)
    def __str__(self):
        if self.istarot :
            showstr = "Người này là Reader"
            return self.username + ' ' + showstr
        return self.username
    

class giao_dich (models.Model ):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE , related_name='user_id'  )
    name = models.CharField(max_length=255,null=True  )
    price = models.IntegerField(null=True)
    date  = models.DateTimeField(null=True)
    user_use = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_use', null=False)
    is_paid = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    def __str__(self):
        trangthai = "chưa thanh toán"
        
        if self.is_paid:
            trangthai = "Đã thanh toán"
        elif self.is_delete and not self.is_paid:
            trangthai = "Đã hủy"
        
        return (
            f"{self.name} giao dịch số {self.id} | User sử dụng dịch vụ {self.user_use.username} được cung cấp bởi "
            f"{self.user_id.username} ||||| trạng thái {trangthai}"
        )
