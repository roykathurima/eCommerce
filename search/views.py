from django.shortcuts import render

from products.models import Product

# Create your views here.
def search_results(request, *args, **kwargs):
	# print(request.GET)
	# print(request.GET.get('q'))
	# print(request)
	query = request.GET.get('q', None)
	obj = Product.objects.search(query)	# print('The Object')
	print(obj)
	context = {
		'object': obj,
		'query':query,
		'count':obj.count(),
	}
	return render(request, "search/search_view.html", context)