from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from accounts import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from accounts.views import PaymentInitiationView, PackageViewSet, webhook, CoinViewSet, PurchaseCryptoView, WalletViewSet, sellcrypto, CryptoTransactionListView, purchasealternative, get_referral_code, CustomUserViewSet, BoughtCryptoTransactionListView, SoldCryptoTransactionListView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Eloquentexchange API",
      default_version='v1',
      description="api endpoint for eloqueunt backend description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="macasorekingdavid@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'package', PackageViewSet)
router.register(r'coin', CoinViewSet)
router.register(r'wallet', WalletViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', views.send_email, name='send-email'),
    path('activate/<str:uid>/<str:token>', views.activate_user, name='activate_user'),
    path(
        "auth/twitter/redirect/",
        views.TwitterAuthRedirectEndpoint.as_view(),
        name="twitter-login-redirect",
   ),
    path('auth/register/', CustomUserViewSet.as_view({'post': 'create'}), name='user-register'),
    path('referralcodecheck/', views.check_referral_code, name='check-referral-code'),
    path('sell/', sellcrypto, name='sell-crypto'),
    path('auth/webhook/', webhook, name='webhook'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('initiate-payment/', PaymentInitiationView.as_view(), name='initiate-payment'),
    path('buy/', PurchaseCryptoView.as_view(), name='buy-crypto'),
    path('crypto-transactions/', CryptoTransactionListView.as_view(), name='crypto-transaction-list'),
    path('crypto-transactions/bought/', BoughtCryptoTransactionListView.as_view(), name='bought-transactions'),
    path('crypto-transactions/sold/', SoldCryptoTransactionListView.as_view(), name='sold-transactions'),
    path('payment_alternative/', purchasealternative, name='payment-alternative'),
    path('referral_code/', get_referral_code, name="referral-code")

]

urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
