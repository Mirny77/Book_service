from django.db import models


class Tag(models.Model):
    name=models.CharField("Название тега",max_length=128, unique=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:

        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'



