from django.db import models
import datetime

# Create your models here.


class Shoe(models.Model):
	name 			= models.CharField(max_length=30, default="Boosts")
	image 			= models.ImageField(upload_to='shoe/', blank=True, null=True)
	style 			= models.CharField(max_length=20, default="sneakers")
	size 			= models.IntegerField(default=10)
	color 			= models.CharField(max_length=20, default="blue")
	brand 			= models.CharField(max_length=20, default="Nike")
	price 			= models.DecimalField(max_digits=4, decimal_places=2, default=4.00)
	availability 	= models.BooleanField(default=True)
	new 			= models.BooleanField(default=True)
	stock 			= models.IntegerField(default=5)
	gender_choices 	= (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	gender 			= models.CharField(max_length=1, choices=gender_choices, default="M")
	date 			= models.DateField(("Date"), default=datetime.date.today)
	like 			= models.BooleanField(default=False)



	def __str__(self):
		return str(self.name)
