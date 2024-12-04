from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404

from product_module.models import Product, ProductGallery
from utils.convertors import group_list


class ProductListView(ListView):
    template_name = 'product_module/product.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context





class ProductDetailView(DetailView):
    template_name = 'product_module/product-detail.html'
    model = Product
    context_object_name = 'product'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug)


    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        loaded_product = self.object
        galleries = list(ProductGallery.objects.filter(product_id=loaded_product.id).all())
        galleries.insert(0, loaded_product)
        context['galleries'] = group_list(galleries,1)
        return context