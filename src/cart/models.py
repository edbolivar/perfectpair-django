from django.db import models

from shoe.models import Shoe
# Create your models here.

class Cart(models.Model):
	products 		= models.ManyToManyField(Shoe, null=True, blank=True)
	total			= models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	availability 	= models.BooleanField(default=True)



	def __str__(self):
		return "Cart id: %s" %(self.id)

