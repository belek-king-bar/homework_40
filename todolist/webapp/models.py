from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50, verbose_name='Задача')
    status = models.CharField(max_length=20, blank=True, default='new', verbose_name='Готовность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    due_date = models.DateTimeField('Выполнить к')


    def __str__(self):
        return f"{self.pk}. {self.name} {(self.status)}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'