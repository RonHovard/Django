from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='категория', max_length=64)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.name}'
