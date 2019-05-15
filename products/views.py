from django.shortcuts import render

from .models import Product

from .forms import ProductForm



def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        #Re-render the form so that it becomes blank after posting data
        form = ProductForm()
    
    context = {        
        'form':form,
    }
    return render(request, "product/create.html", context)

def product_detail_view(request, id, **kwargs):
    obj  = Product.objects.get(id=id)
    context = {
        #'title' : obj.title,
        #'description' : obj.description,
        #'price' : obj.price,

        # we avoid the above and do the below
        # so that we dont have to change code in both the view and template
        # incase a new field is added in the future
        
        'object':obj,
    }
    return render(request, "product/detail.html", context)

def product_list_view(request, *args, **kwargs):
    obj = Product.objects.all()    
    context = {        
        'object':obj,
    }
    return render(request, "product/products.html", context)