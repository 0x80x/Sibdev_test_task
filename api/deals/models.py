from django.db import models
from django.utils.timezone import now


# Наша модель БД

class Deals(models.Model):
    customer = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    total = models.IntegerField(blank=False, null=True)
    quantity = models.IntegerField(blank=False, null=True)
    date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['total']
        verbose_name = 'Сделку'
        verbose_name_plural = 'Сделок'

    def __str__(self):
        return 'Истории сделок'
