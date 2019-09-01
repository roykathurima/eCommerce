from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("title", "price", "description", "featured", "image") 
        widgets = {
        	"title" : forms.TextInput(attrs={"class":"form-control"}),
        }

    #The alternative way to format the widget
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({"class":"form-control"})
        self.fields["description"].widget.attrs.update({"class":"form-control"})
        # self.fields["image"].widget.attrs.update({"class":"btn btn-default"})
        # self.fields["featured"].widget.attrs.update({"class":"form-control"})
