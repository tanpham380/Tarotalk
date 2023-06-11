from django.contrib import admin
from .models import *
# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username',)
class GiaoDichAdmin(admin.ModelAdmin) :
    list_display = ('trangthai_colored','name','price','date')
    search_fields = ('user','ngay_giao_dich','trang_thai')
    ordering = ('id',)
admin.site.register(User,UserAdmin)
admin.site.register(giao_dich,GiaoDichAdmin)