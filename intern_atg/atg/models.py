from django.db import models

# Create your models here.
class URLInformation(models.Model):
	url = models.CharField(max_length = 2048,unique = True)
	is_saved = models.BooleanField(default = False)
	result = models.CharField(max_length=2048)
	class Meta:
		db_table = 'url'

	def __str__(self):
		return self.url 
