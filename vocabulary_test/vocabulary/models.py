from django.db import models

class Word(models.Model):
	prob = models.TextField(default='')
	ans = models.TextField(default='')
	all_count = models.PositiveIntegerField(default=0)
	correct_count = models.PositiveIntegerField(default=0)
