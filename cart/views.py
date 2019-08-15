from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart

# Create your views here.
# I'll start with a function based view

def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	return render(request, "carts/home.html", {'cart':cart_obj})

def cart_update(request):
	print(request.POST)
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show user that Product is gone")
			return redirect("../cart/")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)

		print(cart_obj.total)
	#alternatively; cart_obj.products.add(product_id)
	# return redirect(product_obj.get_absolute_url())
	return redirect("../cart/")
# def cart_create(user=None):
# 	cart_obj = Cart.objects.create(user=None)
# 	print('Created Cart')
# 	return cart_obj

# def cart_home(request):
# 	#del request.session['cart_id']
# 	cart_id = request.session.get('cart_id', None)
# 	# if cart_id is None:
# 	# 	cart_obj = cart_create()
# 	# 	request.session['cart_id'] = cart_obj.id
# 	# 	print(cart_id)		
# 	# else:
# 	qs = Cart.objects.filter(id=cart_id)
# 	if qs.count() == 1:
# 		print('cart object exists')
# 		cart_obj = qs.first()
# 		print(cart_id)
# 		if request.user.is_authenticated and cart_obj.user is None:
# 			cart_obj.user = request.user
# 			cart_obj.save()
# 		# print(cart_id)
# 	else:
# 		cart_obj = Cart.objects.new(request.user)
# 		request.session['cart_id'] = cart_obj.id
# 	# print(request.session)
# 	# print(dir(request.session))
# 	# print(request.session.session_key)
# 	return render(request, "carts/home.html", {})
