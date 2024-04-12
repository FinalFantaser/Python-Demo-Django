from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.IntegerField(verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-date']

    def __str__(self):
        return 'Заявка'
