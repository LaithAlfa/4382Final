from django.urls import path

from .views import HomePageView, AboutPageView, SocksPageView, StocksPageView, PurchasePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index.html/', HomePageView.as_view(), name='home'),
    path('about.html/', AboutPageView.as_view(), name='about'),
    path('socks.html/', SocksPageView.as_view(), name='socks'),
    path('stocks.html/', StocksPageView.as_view(), name='stocks'),
    path('purchase.html/', PurchasePageView.as_view(), name='purchase'),
]