from django.db import models

class Youser(models.Model):
	pass
	
class Item(models.Model):
	youId=models.ForeignKey(Youser, default=None, on_delete=models.CASCADE)
	text=models.TextField (default="")
	feelId=models.TextField (default="")
	codeId=models.TextField (default="")
	descId=models.TextField (default="")
	


# Create your models here.
