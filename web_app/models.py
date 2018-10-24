from django.db import models



class expenses(models.Model):
    name = models.CharField(max_length=25)
    income = models.IntegerField()
    expense = models.IntegerField()
    savings = models.IntegerField()
