from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Expense(models.Model):
    now = datetime.now()
    Date = models.DateTimeField()
    txt = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    usr = models.ForeignKey(User,on_delete=models.PROTECT) 

