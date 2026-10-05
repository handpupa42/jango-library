from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
         User, on_delete=models.CASCADE, related_name='profile'
    )
    phone = models.CharField(
         max_length=20, blank=True, null=True, verbose_name='Телефон'
    )
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')
    birth_date = models.DateField(
         blank=True, null=True, verbose_name='Дата рождения'
    )
    library_card_number = models.CharField(
         max_length=50,
         unique=True,
         blank=True,
         null=True,
         verbose_name='Номер читательского билета',
    )
    created_at = models.DateTimeField(
         auto_now_add=True, verbose_name='Дата регистрации'
    )

    def __str__(self):
       return f'Профиль пользователя: {self.user.username}'
