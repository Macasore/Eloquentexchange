from django.contrib import admin
from .models import UserAccount, Payment, Package

admin.site.register(UserAccount)
admin.site.register(Package)
admin.site.register(Payment)
# Register your models here.
