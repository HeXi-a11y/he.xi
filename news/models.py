from django.db import models

class Articles(models.Model):
    title = models.CharField('Название',max_length=25)
    desc = models.CharField('Описание',max_length=50)
    fullText = models.TextField('Пост')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f''

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

# Create your models here.
