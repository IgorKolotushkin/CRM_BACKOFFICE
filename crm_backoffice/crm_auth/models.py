from django.contrib.auth.models import User
from django.db import models


class RoleUser(models.Model):
    ROLES = (
        ('Administrator', 'Administrator'),
        ('Operator', 'Operator'),
        ('Marketer', 'Marketer'),
        ('Manager', 'Manager'),
    )

    user = models.OneToOneField(User, related_name="role", on_delete=models.CASCADE)
    role = models.CharField(choices=ROLES, null=False)

    def __str__(self):
        return self.role

