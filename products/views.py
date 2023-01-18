from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Products, Categories


class ProductsListView(generic.TemplateView):
    template_name = 'products/products_list.html'

    def get_queryset(self):
        products = Products.objects.all()
        return products

    def get_context_data(self, **kwargs):
        if self.request.GET.get('category'):
            products = Products.objects.filter(category__name=self.request.GET['category'])
        else:
            products = Products.objects.all()
        categories = Categories.objects.all()
        context = {
            'products': products,
            'categories': [category.name for category in categories]
        }
        return context
