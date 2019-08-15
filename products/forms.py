from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("title", "price", "description", "featured") 
        widgets = {
        	"title" : forms.TextInput(attrs={"class":"form-control"}),
        }

    #The alternative way to do it
    def __init__(self, *args, **kwargs):
    	super().__init__(*args, **kwargs)
    	self.fields['price'].widget.attrs.update({"class":"form-control"})
    	self.fields["description"].widget.attrs.update({"class":"form-control"})
    	# self.fields["featured"].widget.attrs.update({"class":"form-control"})
