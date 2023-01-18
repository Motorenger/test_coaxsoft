from django.urls import path


from . import views


app_name = 'products'
urlpatterns = [
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/order_html', views.ProductOrderHTMLView.as_view(), name='product_order_html'),
    path('products/<int:pk>/order_jquery', views.UserCountView.as_view(), name='product_order_jquery')
]
