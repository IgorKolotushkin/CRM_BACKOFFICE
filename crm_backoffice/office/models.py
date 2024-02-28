"""Модуль с моделями для CRM"""

from django.db import models


def upload_directory_path(instance, filename):
    """
    Функция для указания пути загрузки файла
    :param instance:
    :param filename: имя файла
    :return: путь загрузки файла
    """
    return f'upload/name_{instance.name}/{filename}'


class Lead(models.Model):
    """
    Класс модель для описания потенциального клиента.
    """
    first_name: str = models.CharField(max_length=30, null=False)
    last_name: str = models.CharField(max_length=50, null=False)
    email: str = models.EmailField(max_length=50, null=False, unique=True)
    phone: str = models.CharField(max_length=12, null=False, blank=False)
    ads: models.ForeignKey = models.ForeignKey('Ads', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        """
        Метод для вывода человекочиаемого названия потенциального клиента
        :return: имя и фамилия клиента
        """
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    """
    Класс модель для описания активного клиента.
    """
    lead: models.ForeignKey = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contract: models.ForeignKey = models.ForeignKey('Contract', on_delete=models.CASCADE, null=True, blank=True)


class Product(models.Model):
    """
    Класс модель для описания продукта.
    """
    name: str = models.CharField(max_length=100, null=False, blank=False)
    description: str = models.TextField()
    cost: float = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        """
        Метод для вывода человекочиаемого названия продукта.
        :return: Название продукта
        """
        return f"{self.name}"


class Ads(models.Model):
    """
    Класс модель для описания рекламы.
    """
    name: str = models.CharField(max_length=100, null=False, blank=False)
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.CASCADE)
    channel: str = models.CharField(max_length=50)
    budget: float = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        """
        Метод для вывода человекочиаемого названия рекламы.
        :return: Название рекламы
        """
        return f"{self.name}"


class Contract(models.Model):
    """
    Класс модель для описания контракта.
    """
    name: str = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost: float = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    file = models.FileField(upload_to=upload_directory_path, blank=True)

    def __str__(self) -> str:
        """
        Метод для вывода человекочиаемого названия контракта.
        :return: Название контракта
        """
        return self.name
