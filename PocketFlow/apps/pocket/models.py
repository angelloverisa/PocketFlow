from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.BooleanField()
    def __str__(self):
        return self.name # this is so the class automatically named "transportation, foods"
                        #instead of "category 1, category 2"

class Account(models.Model):
    account_type = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    balance = models.FloatField()
    currency = models.CharField(max_length=100)
    def __str__(self):
        return self.account_name

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=100) # debit atau credit
    amount = models.FloatField()
    notes = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

