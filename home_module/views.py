from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView

from product_module.models import Product, ProductGallery
from utils.convertors import group_list


# Create your views here.

# def home(request):
#     return render(request, 'home_module/index.html')
#

class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context =super(HomeView, self).get_context_data(**kwargs)
        latest_product = Product.objects.filter(is_active=True, is_deleted=False).order_by('-id')[:12]
        context['short_product_name'] = Product.objects
        context['latest_product'] = group_list(latest_product,5)
        return context