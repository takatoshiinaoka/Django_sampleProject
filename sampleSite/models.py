from django.db import models

class Kweet(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

class Kakeibo(models.Model):
    date = models.DateTimeField()
    opt = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    suuji = models.IntegerField()

    