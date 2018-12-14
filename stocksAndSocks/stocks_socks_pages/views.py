from django.views.generic import TemplateView

from products.models import Product, Buyer, Payment


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SocksPageView(TemplateView):
    model = Product
    template_name = 'socks.html'

class StocksPageView(TemplateView):
    model = Product
    template_name = 'stocks.html'

class PurchasePageView(TemplateView):
    model = Buyer
    model = Payment
    template_name = 'purchase.html'
    fields = ['']