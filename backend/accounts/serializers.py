from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Payment, Package, Coin, BuyCrypto, Wallets, SellCrypto, ReferralCode, UserAccount
import string
import random
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class ReferralSerializer(serializers.Serializer):
    referral_code = serializers.CharField()
    
    def validate(self, data):
        print("it got here")
        if not ReferralCode.objects.filter(code=data.get('referral_code')).exists():
            raise serializers.ValidationError("Referral code is invalid")
        return data
    
    def update(self, data):
        referral_code = data.get('referral_code')
        referrer = ReferralCode.objects.get(code=referral_code)

        referrer.usage_count += 1
        referrer.save()

        # Generate a new referral code for the user and associate it with them
    
        
        
class UserCreateSerializercustom(UserCreateSerializer):
    referral_code = ReferralSerializer(required=False)
    class Meta(UserCreateSerializer):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'referral_code']
        
    def create(self, request, *args, **kwargs):
        print("it got here too")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Your custom registration logic here

        # Call the parent class's create method to complete the registration
        user = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

        
        
class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    message = serializers.CharField()
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ('id', 'name', 'price')
        
class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'name', 'buy_rate', 'sell_rate')
        
class BuyCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyCrypto
        fields = ['id', 'coin_type', 'amount', 'status', 'date', 'trans_type']
        
class SellCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellCrypto
        fields = ['id', 'amount', 'status', 'date', 'trans_type', 'coin_type', 'account_number', 'bank', 'sender_address']
        
class SellCryptoSerializerfilter(serializers.ModelSerializer):
    class Meta:
        model = SellCrypto
        fields = ['id', 'amount', 'status', 'date', 'trans_type', 'coin_type']
        
        
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ['id', 'coin', 'network', 'address']
        
        
class CombinedCryptoSerializer(serializers.Serializer):
    # buy_id = serializers.IntegerField(source='id')
    # buy_amount = serializers.DecimalField(max_digits=15, decimal_places=2, source='amount')
    # buy_coin_type = serializers.CharField(source='coin_type')
    # buy_status = serializers.CharField(source='status')
    # buy_date = serializers.DateTimeField(source='date')
    # buy_transtype = serializers.CharField(source='trans_type')
    # buy_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    
    # sell_id = serializers.IntegerField(source='id')
    # sell_amount = serializers.DecimalField(max_digits=15, decimal_places=2, source='amount')
    # sell_status = serializers.CharField(source='status')
    # sell_date = serializers.DateTimeField(source='date')
    # sell_transtype = serializers.CharField(source='trans_type')
    # sell_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    # sell_coin_type = serializers.CharField(source='coin_type')
    # sell_account_number = serializers.IntegerField(source='account_number')
    # sell_bank = serializers.CharField(source='bank')
    
    # def to_representation(self, instance):
        
    #     combined_data = {
    #         'buy_id': instance.buy_data.id,
    #         'buy_amount': instance.buy_data.amount,
    #         'buy_coin_type': instance.buy_data.coin_type,
    #         'buy_status': instance.buy_data.status,
    #         'buy_date': instance.buy_data.date,
    #         'buy_transtype': instance.buy_data.transtype,
    #         'sell_id': instance.sell_data.id,
    #         'sell_amount': instance.sell_data.amount,
    #         'sell_date': instance.sell_data.date,
    #         'sell_status': instance.sell_data.status,
    #         'sell_transtype': instance.sell_data.transtype,
    #         'sell_coin_type': instance.sell_data.coin_type,
    #         'sell_account_number': instance.sell_data.account_number,
    #         'sell_bank': instance.sell_data.bank
    #     }
    #     return combined_data
    buy_data = BuyCryptoSerializer()
    sell_data = SellCryptoSerializerfilter()
    
    
    
