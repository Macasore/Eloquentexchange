from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

PLAN_CHOICES = (
    ("BEGINNERS", "Beginners"),
    ("INTERMEDIATE", "Intermediate"),
    ("PRO", "Pro"),
)

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        
        user.save()
        return user
    
    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def get_full_name(self):
        return self.first_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email


class Payment(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    email = models.EmailField()
    reference = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    package = models.CharField(max_length=20, choices=PLAN_CHOICES)
    
    def __str__(self):
        return f"Payment {self.reference}"
    
    
class Package(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    
    def __str__(self):
        return self.name