from django.shortcuts import render, HttpResponseRedirect


# Create your views here.

from shoe.models import Shoe
from .models import Cart

def view(request):

	cart = Cart.objects.all()
	context = {"cart": cart}
	template = "cart/view.html"
	return render(request, template, context)

