from django.db import models

# Create your models here.
class customer(models.Model):
    cust_id = models.CharField(max_length=100)
    cust_fname=models.CharField(max_length=100)
    cust_lname=models.CharField(max_length=100)
    last_transaction_date=models.DateField(max_length=100)
    ac_balance=models.CharField(max_length=100)
    ac_opening_date=models.DateField(max_length=100)

    def __str__(self):
        return self.cust_id
    
class product(models.Model):
    prod_id=models.CharField(max_length=100)
    cust_id=models.CharField(max_length=100)
    cross_sell=models.CharField(max_length=100)

    def __str__(self):
        return self.prod_id