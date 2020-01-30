from django.db import models

class Search(models.Model):
	sequence = models.TextField(); 
	proteinName = models.TextField();
	proteinIndex = models.IntegerField(); #Where it was found