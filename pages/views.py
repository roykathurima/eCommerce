from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text":"This is an eCommerce site in the making",
        "my_number" : +254711836533
    }
    return render(request, "about.html", my_context)
