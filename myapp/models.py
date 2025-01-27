from django.db import models
# Create your models here.

from django.core.validators import RegexValidator

class UserRegister(models.Model):
    name = models.CharField(max_length=50, default="Default Name")  # Default added
    password = models.CharField(max_length=50, default="default_password")  # Default added
    email = models.EmailField(null=True, blank=True)  # Optional field
    mob = models.CharField(
        max_length=10,
        default="1234567890",
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Mobile number must be 10 digits.",
                code="invalid_mobile",
            )
        ],
    )
    add = models.TextField(default="Default Address")
    def __str__(self):
        return self.name
class employeedetails(models.Model):

    user = models.ForeignKey(UserRegister, on_delete=models.SET_NULL, null=True, blank=True)
    empcode = models.CharField(max_length=50,null=True)
    empdept = models.CharField(max_length=100,null=True)
    destination = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningdate = models.DateField(null=True)

    def __str__(self):
        return self.user.name