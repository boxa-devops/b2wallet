from django.db import models


class Transaction(models.Model):
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)
