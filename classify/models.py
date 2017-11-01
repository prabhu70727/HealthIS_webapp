from django.db import models

# Create your models here.
class Classification(models.Model):
    title = models.CharField(max_length=200)

    def classify(self):
    	#TODO
        return

    def display(self):
    	#TODO
        return    

    def __str__(self):
        return self.title