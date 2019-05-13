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
		products = Shoe.objects.filter(brand__icontains=q)	
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
	q1 = request.GET.get('Adidas')
	q2 = request.GET.get('Nike')
	q3 = request.GET.get('Puma')
	f1 = "Adidas" if q1 == "on" else "1"
	f2 = "Nike" if q2 == "on" else "1"
	f3 = "Puma" if q3 == "on" else "1"
	q4 = request.GET.get('s10')
	q5 = request.GET.get('s9')
	q6 = request.GET.get('s8')
	f4 = 10 if q4 == "on" else 0
	f5 = 9 if q5 == "on" else 0
	f6 = 8 if q6 == "on" else 0
	q7 = request.GET.get('blue')
	q8 = request.GET.get('black')
	q9 = request.GET.get('red')
	f7 = "blue" if q7 == "on" else "1"
	f8 = "black" if q8 == "on" else "1"
	f9 = "red" if q9 == "on" else "1"
	print(f7)
	q10 = request.GET.get('d10')
	q11 = request.GET.get('d9')
	q12 = request.GET.get('d8')
	f10 = 10 if q10 == "on" else 0
	f11 = 9 if q11 == "on" else 0
	f12 = 8 if q12 == "on" else 0

	products1 = Shoe.objects.filter(Q(brand__icontains=f1)|Q(brand__icontains=f2)|Q(brand__icontains=f3))
	products2 = Shoe.objects.filter(Q(size__exact=f4)|Q(size__exact=f5)|Q(size__exact=f6))
	products3 = Shoe.objects.filter(Q(color__icontains=f7)|Q(color__icontains=f8)|Q(color__icontains=f9))
	products4 = Shoe.objects.filter(Q(price__exact=f10)|Q(price__exact=f11)|Q(price__exact=f12))
	products = []
	if(products1):
		products = products1
	if(products2):
		products = products & products2
	if(products3):
		products = products & products3
	if(products4):
		products = products & products4
	
	context = {'products': products}
	template = 'shoe/sidebar.html'

	# if q == "on":
	# 	q = "Adidas"
	# else:
	# 	return render(request, 'shoe/sidebar.html', {})
	# if q:

	# elif q == '':
	# 	template = 'shoe/sidebar.html'
	# 	context = {}
	# else:
	# 	template = 'shoe/sidebar.html'
	# 	context = {}
		
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



    	



































