from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()

class Advertisement(models.Model):
    image = models.ImageField('изображение', upload_to = 'advertisements/')
    
    title = models.CharField('заголовок', max_length=128)
    
    description = models.TextField('описание')

    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    auction = models.BooleanField('торг', help_text='Отметьте, если хотите торговаться')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, verbose_name= 'Пользователь', on_delete=models.CASCADE)



    class Meta:
        db_table = 'advertisements'


    @admin.display(description= "Дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():

            created_date = self.created_at.strftime("%H.%M.%S")
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} </span>', created_date)
        return self.created_at.strftime("%d.%m.%Y в %H.%M.%S")
    
    @admin.display(description= "ИЗОБРАЖЕНИЕ")
    def get_html_image(self):
        if self.image:
            return format_html('<img src = "{}" style = "max-width:80px; max-height:80px"', self.image.url)



    @admin.display(description= "Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():

            created_date = self.created_at.strftime("%H.%M.%S")
            return format_html('<span style = "color:green; font-weight: bold"> Сегодня в {} </span>', created_date)
        return self.created_at.strftime("%d.%m.%Y в %H.%M.%S")
    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, price = {self.price}, image = {self.image})'
    




