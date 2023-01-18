from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response


from .models import Products, Categories
from .forms import OrderForm
from .serializers import OrderSerializer


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


class ProductOrderHTMLView(generic.edit.FormView):
    form_class = OrderForm
    template_name = 'products/order_product_html.html'

    def form_valid(self, form):
        product = get_object_or_404(Products, id=self.kwargs["pk"])

        form.instance.product_name = product.name
        form.instance.category = product.category
        form.instance.price = product.price

        form.save()
        return HttpResponseRedirect(reverse('products:products_list'))


class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request, pk):
        form = OrderForm()
        return Response({'form': form}, template_name='products/order_product_jquery.html')

    def post(self, request, pk):
        print(self.POST)
        print(self.data)

