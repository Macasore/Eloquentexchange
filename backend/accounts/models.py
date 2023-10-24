from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import string
import random

PLAN_CHOICES = (
    ("BEGINNERS", "Beginners"),
    ("INTERMEDIATE", "Intermediate"),
    ("PRO", "Pro"),
)

COIN_CHOICES = (
    ("USDT", "Usdt"),
    ("BTC", "Btc"),
    ("ETH", "Eth"),
)

TRANS_OPTIONS = (
    ("BOUGHT", "Bought"),
    ("Sold", "Sold")
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
    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)
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
    
    # def save(self, *args, **kwargs):
    #     if not self.referral_code:
    #         self.referral_code = self.generate_referral_code()
    #     super().save(*args, **kwargs)
        
    #     ReferralCode.objects.create(code=self.referral_code, owner=self)

    


class Payment(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    reference = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    package = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Payment {self.reference}"
    
    
class Package(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Coin(models.Model):
    name = models.CharField(max_length=20)
    buy_rate = models.DecimalField(max_digits=100, decimal_places=2)
    sell_rate = models.DecimalField(max_digits=100, decimal_places=2)
    
    
    def __str__(self):
        return self.name
    
class Wallets(models.Model):
    coin = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.coin
    
class BuyCrypto(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    reference = models.CharField(max_length=100)
    coin_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    trans_type = models.CharField(max_length=20)
    network = models.CharField(max_length=20)
    wallet_address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.coin_type
    
class SellCrypto(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    trans_type = models.CharField(max_length=20)
    coin_type = models.CharField(max_length=50)
    account_number = models.IntegerField()
    bank = models.CharField(max_length=20)
    sender_address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.coin_type
    
class ReferralCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    owner = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    usage_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.referrer
    
    