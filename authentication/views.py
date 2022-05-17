from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from products.models import Product

from .forms import LoginForm, RegisterForm

# Create your views here.

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {        
        'form':form,
    }
	# print(dir(request.method))
	# print(request.user.is_authenticated)
	# print(request)
	if request.method == 'GET':
		context['cred'] = True
		print("method is get")
	if form.is_valid():
		print(form.cleaned_data)
		context['data'] = form.cleaned_data
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#Redirect to a success page
			context['form'] = LoginForm()
			# print('successfully logged in')
			return redirect("product-list")
		else:
			print('we are here')
			context['form'] = LoginForm()
		# else:
		# 	#Return an 'invalid login' error message
		# 	context['form'] = LoginForm() 
		# 	# print("Error")
		# 	context['cred'] = True
		# 	# print(context['cred'])
	return render(request, "authentication/login.html",context)

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {        
        'form':form,
    }
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		email = form.cleaned_data.get('email')
		new_user = User.objects.create_user(username, email, password)
		context['form'] = RegisterForm() 
		# print(new_user)
	return render(request, "authentication/register.html",context)

def log_out(request):
	logout(request)
	return redirect('log_in')