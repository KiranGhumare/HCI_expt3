from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Customer(models.Model):
# 	# GENDER=(('Male', 'Male'),
# 	# 	('Female','Female'),
# 	# 	('Other','Other')
# 	# 	)
# 	user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
# 	# first_name = models.CharField(max_length=200, null=True)
# 	# last_name = models.CharField(max_length=200, null=True)
# 	# email = models.CharField(max_length=200, null=True)
# 	# date_created= models.DateTimeField(auto_now_add=True, null=True)
# 	# username = models.CharField(max_length=200, null=True)
# 	# phone = models.CharField(max_length=12, null=True)
# 	# gender = models.CharField(max_length=100,null=True, choices=GENDER)
# 	# age= models.CharField(max_length=200, null=True)
# 	# profile_pic=models.ImageField(default="profile_aBGztjN.png",null=True,blank=True)
# 	# ap=models.ForeignKey(app_of_Patient,null=True,on_delete=SET_NULL)
	
# 	def __str__(self):
# 		return self.user.username