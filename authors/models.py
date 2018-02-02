from django.db import models


class Author(models.Model):
    name=models.CharField("Имя",max_length=64)
    surname=models.CharField("Фамилия",max_length=64)
    patronymic=models.CharField("Отчество",max_length=64,blank=True, null=True, default=None)
    phone= models.CharField("Телефон",max_length=11,blank=True, null=True, default=None)
    email=models.EmailField("Эл. адрес",blank=True, null=True, default=None)

    def __str__(self):
        return "%s, %s" % (self.name, self.surname)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'






