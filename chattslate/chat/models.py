from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
	host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	script = models.TextField(null=True, blank=True)
	chat_begin_datetime = models.DateTimeField(auto_now_add=True)
	chat_end_datetime = models.DateTimeField(null=True)
	active = models.BooleanField(null=True)
	#participants = 
	
	def __str__(self):
		return str(self.name)

class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.body[0:50]

		