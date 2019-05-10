from django.shortcuts import render

# Create your views here.

def show(request):

	template = 'customerservice/cs_form.html'
	context = {}

	return render(request, template, context)


def pricing(request):

	template = 'customerservice/pricing_form.html'
	context = {}

	return render(request, template, context)


def faq(request):

	template = 'customerservice/faq.html'
	context = {}

	return render(request, template, context)