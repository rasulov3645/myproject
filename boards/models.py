from django.db import models


from django.contrib.auth.models import User 
# Create your models here.


class Board(models.Model): 
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)



class Topic(models.Model): 
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeingKey(Board, related_name='topics')
	starter = models.ForeingKey(User, related_name='topics')


class Post(models.Model): 
	message = models.TextField(max_length=4000)
	topic = models.ForeingKey(Topic, related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeingKey(User, related_name='posts')
	updated_by = models.ForeingKey(User, null=True, related_name='+')
