from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Categories(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Categories, related_name="products", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="products", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Orders(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    product_name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.username}'s order"
