from django.contrib import admin
from .models import UserRegister

# Register your models here.

class userreg_(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','password','mob', 'add']
    # def Confirm_password(self, obj):
    #     # Replace with actual logic to display password confirmation status
    #     return 'Confirmed' if obj.password == obj.password_confirmation else 'Not Confirmed'
    
admin.site.register(UserRegister, userreg_)

