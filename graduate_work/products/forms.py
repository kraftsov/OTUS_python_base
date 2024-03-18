from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "category",
            # "sub_category",
            "name",
            "description",
            # "stock",
            "price",
            # "featured",
            # "image_url",
            "image",
            # "sku"
        }
