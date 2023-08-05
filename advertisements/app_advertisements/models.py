from django.db import models
from django.contrib import admin
from django.utils.html import format_html
# Create your models here.


class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    
    description = models.TextField('описание')

    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    auction = models.BooleanField('торг', help_text='Отметьте, если хотите торговаться')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'


    @admin.display(description= "Дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():

            created_date = self.created_at.strftime("%H.%M.%S")
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} </span>', created_date)
        return self.created_at.strftime("%d.%m.%Y в %H.%M.%S")



    @admin.display(description= "Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():

            created_date = self.created_at.strftime("%H.%M.%S")
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} </span>', created_date)
        return self.created_at.strftime("%d.%m.%Y в %H.%M.%S")
    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, price = {self.price})'
    




