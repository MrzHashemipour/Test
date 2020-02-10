from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    Date = models.DateTimeField()
    txt = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    usr = models.ForeignKey(User,on_delete=models.PROTECT) 

    def __str__(self):
        return "{}---{}---{}".format(self.txt, self.Date, self.amount)
        #return self.txt

class Income(models.Model):
    Date = models.DateTimeField()
    txt = models.CharField(max_length = 255)
    amount = models.BigIntegerField()
    usr = models.ForeignKey(User,on_delete = models.PROTECT)
    def __str__(self):
        return "{}---{}---{}".format(self.txt, self.Date, self.amount)