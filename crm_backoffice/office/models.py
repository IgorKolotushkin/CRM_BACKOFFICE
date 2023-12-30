from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(max_length=12, null=False, blank=False)


class Lead(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    # ads = models.
