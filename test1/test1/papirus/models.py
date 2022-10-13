from django.db import models
from django.urls import reverse
from django.utils import timezone


class Papirus(models.Model):
    name = models.CharField(max_length=40)  # Исполнитель
    where = models.CharField(max_length=40)  # Откуда
    initiator = models.CharField(max_length=40)  # Инициатор
    type_documents = models.CharField(max_length=40)  # Тип документа
    registr_number = models.CharField(max_length=20)  # Регистрационный номер
    time_create = models.DateTimeField(auto_now_add=True)
    complate_status = models.CharField(max_length=40)  # Статус выполнения
    cat = models.ForeignKey('Name', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Name(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('name', kwargs={'post_id': self.pk})
