from django.db import models


def upload_directory_path(instance, filename):
    return 'upload/name_{0}/{1}'.format(instance.name, filename)


class Lead(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    ads = models.ForeignKey('Ads', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    channel = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    file = models.FileField(upload_to=upload_directory_path)

    def __str__(self):
        return self.name
