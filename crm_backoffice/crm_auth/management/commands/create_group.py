"""Модуль с командами для администратора"""
from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand

perms_managers: list = [
    'Can add contract',
    'Can change contract',
    'Can view contract',
    'Can add customer',
    'Can view customer',
    'Can view lead',
    'Can view ads',
]

perms_marketers: list = [
    'Can add ads',
    'Can change ads',
    'Can view ads',
    'Can add product',
    'Can change product',
    'Can view product',
]

perms_operators: list = [
    'Can add lead',
    'Can change lead',
    'Can view lead',
    'Can view ads',
]

groups_with_perms: dict[str, list[str]] = {
    'managers': perms_managers,
    'marketers': perms_marketers,
    'operators': perms_operators,
}


class Command(BaseCommand):
    """
    Создание групп
    """
    def handle(self, *args, **options) -> None:
        self.stdout.write("Создание групп ...")

        for group in groups_with_perms.items():
            name_group: Group = Group.objects.create(name=group[0])
            for perm in group[1]:
                name_perm: Permission = Permission.objects.get(name=perm)
                name_group.permissions.add(name_perm)

            self.stdout.write(f"Создана группа: {name_group}")
