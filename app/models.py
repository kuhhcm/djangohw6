from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return f'{self.title} {self.id}'
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        
