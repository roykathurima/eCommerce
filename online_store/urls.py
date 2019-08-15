"""online_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from search.views import search_results
from pages.views import home_view, about_view
from cart.views import cart_home, cart_update
from products.views import product_create_view, product_list_view, product_s_detail_view #product_detail_view
from authentication.views import login_page, register_page, log_out
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name='log_in'),
    # path('accounts', include('django.contrib.auth.urls')),
    path('', home_view, name='home'),
    # path('products/<int:id>/', product_detail_view, name='product-detail'),
    path('products/<slug:slug>/', product_s_detail_view, name='slug-detail'),
    path('create/', product_create_view, name='product-create' ),
    path('products/', product_list_view, name='product-list'),
    path('logout/', log_out),
    path('cart/', cart_home),
    path('search/', search_results, name='search-results'),
    path('update/', cart_update, name='update'),
    path('register/', register_page),
    path('about/', about_view, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)