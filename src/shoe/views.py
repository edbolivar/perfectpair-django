from django.db.models import Q
from .models import Shoe
from cart.models import Cart
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.


def shoe_list(request):

	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/shoe_list.html', context)


def liked_list(request):


	shoe_list = Shoe.objects.filter(like=True)

	context = {
		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/liked_list.html', context)


def cart_list(request, shoe_id):

	system = request.POST.get('cart', None)
	shoe = get_object_or_404(Shoe, pk=shoe_id)
	cart = Cart.objects.get(pk=2)
	cart.products.add(shoe)
	cart.save()
	shoe_list = []
	for shoe in cart.products.all():
		print(shoe)
		shoe_list.append(shoe)
	print(shoe_list)
	
	# shoe_list = Shoe.objects.all()
	context = {
		'shoe_list': shoe_list,
		'system': system,
	}

	return render(request, 'shoe/cart_list.html', context)



def gender_male(request):


	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/gender_male.html', context)


def gender_female(request):


	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/gender_female.html', context)


def search(request):
	
	q = request.GET.get('q')
	
	if q:
		products = Shoe.objects.filter(name__icontains=q)
		context = {'query': q, 'products': products}
		template = 'shoe/gender_male.html'

	elif q == '':
		template = 'home.html'
		context = {}
	else:
		template = 'home.html'
		context = {}
	return render(request, template, context)

def add_to_cart(request, shoe_id):
	shoe = get_object_or_404(Shoe, pk=shoe_id)

	context = {"shoe":shoe}

	return render(request, template, context)

def new_arrivals(request):
	template = ''
	context = {}

	return render(request, template, context)


def sidebar(request):
	template = 'shoe/sidebar.html'
	context = {}

	return render(request, template, context)


def men_sneakers(request):
    	
	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list, }

	template = 'shoe/men_sneakers.html'
	
	return render(request, template, context)


def men_business(request):
    	
	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	template = 'shoe/men_business.html'
	

	return render(request, template, context)


def men_casual(request):
    	
	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	template = 'shoe/men_casual.html'
	

	return render(request, template, context)


def men_boots(request):
    	
	system = request.POST.get('cart', None)

	shoe_list = Shoe.objects.all()
	
	context = {
		'shoe_list': shoe_list,
		'system': system,
		
	}

	template = 'shoe/men_boots.html'
	return render(request, template, context)


def men_sandals(request):
    
	template = 'shoe/men_sandals.html'
	shoe_list = Shoe.objects.all()
	context = {
		'shoe_list': shoe_list,
	}
	

	return render(request, template, context)


def women_sneakers(request):
	template = 'shoe/women_sneakers.html'
	shoe_list = Shoe.objects.all()
	context = {

		'shoe_list': shoe_list,
	}

	return render(request, template, context)


def women_flats(request):
	template = 'shoe/women_flats.html'
	shoe_list = Shoe.objects.all()
	context = {
		'shoe_list': shoe_list,
	}

	return render(request, template, context)


def women_pumps(request):
	template = 'shoe/women_pumps.html'
	shoe_list = Shoe.objects.all()
	context = {

		'shoe_list': shoe_list,
	}

	return render(request, template, context)


def women_boots(request):
	template = 'shoe/women_boots.html'
	shoe_list = Shoe.objects.all()
	context = {

		'shoe_list': shoe_list,
	}

	return render(request, template, context)


def women_sandals(request):
	template = 'shoe/women_sandals.html'
	shoe_list = Shoe.objects.all()
	context = {

		'shoe_list': shoe_list,
	}

	return render(request, template, context)


def new_arrivals(request):
	template = 'shoe/new_arrivals.html'
	shoe_list = Shoe.objects.all()
	
	context = {

		'shoe_list': shoe_list,
	}

	return render(request, template, context)


def like(request, shoe_id):
	template = 'shoe/like.html'
	shoe = Shoe.objects.get(pk=shoe_id)
	shoe.like = not shoe.like
	shoe.save()
	if shoe.like == True:
		template = 'shoe/liked_list.html'
	shoe_list = Shoe.objects.filter(like=True)

	context = {
		'shoe_list': shoe_list,
	}

	return render(request, template, context)



    	



































