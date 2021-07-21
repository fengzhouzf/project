from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
	"""docstring for ArticlePost"""
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)
