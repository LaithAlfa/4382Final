from django.views.generic import TemplateView

from products import models

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SocksPageView(TemplateView):
    # model = Product # Still working to join model to views (p. 84)
    template_name = 'socks.html'

class StocksPageView(TemplateView):
    template_name = 'stocks.html'

class PurchasePageView(TemplateView):
    template_name = 'purchase.html'
