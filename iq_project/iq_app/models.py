from django.db import models
from django.contrib.auth.models import User
from uuidfield import UUIDField

# Create your models here.
class Registration(models.Model):
	user = models.OneToOneField(User)
	# firstname = models.CharField(max_length=32)
	# username = models.CharField(max_length=32)
	# email = models.EmailField(max_length=32)
	# password = models.CharField(max_length=40)
	age = models.IntegerField(max_length=5)

	def __str__(self):
		return self.user.username


class Solution(models.Model):
	serial_num = models.IntegerField()
	question = models.CharField(max_length=100)
	option1 = models.CharField(max_length=30)
	option2 = models.CharField(max_length=30)
	option3 = models.CharField(max_length=30)
	option4 = models.CharField(max_length=30)
	answer = models.CharField(max_length=30)
	uuid = UUIDField(auto=True)

	def __str__(self):
		return self.question
