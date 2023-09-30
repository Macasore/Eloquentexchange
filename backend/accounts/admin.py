from django.contrib import admin
from .models import UserAccount, Payment, Package, Coin, BuyCrypto, Wallets

admin.site.register(UserAccount)
admin.site.register(Package)
admin.site.register(Payment)
admin.site.register(Coin)
admin.site.register(BuyCrypto)
admin.site.register(Wallets)
# Register your models here.
