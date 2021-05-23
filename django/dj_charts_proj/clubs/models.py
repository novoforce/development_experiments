from django.db import models

# Create your models here.
class Club(models.Model):
    name= models.CharField(max_length=220)
    money= models.IntegerField()

    def __str__(self) -> str:
        return "{}-{}".format(self.name,self.money)