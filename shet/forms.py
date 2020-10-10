from django import forms 
from .models import ProductLink,Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductLink
        fields = '__all__'
        labels = {
            'link':'Google Sheet Link',
        }

class ProductFormCol(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


        
    