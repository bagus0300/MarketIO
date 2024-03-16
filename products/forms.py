from django.forms import ModelForm
from django import forms
from .models import Product, ProductImage, ProductVariant

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'border-primary border-2 h-12 p-2 w-full mb-2'})
            
        self.fields['is_featured'].widget.attrs.update({'class': 'border-primary border-2'})


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        
class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = []