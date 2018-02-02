from django.db import models
from authors.models import Author
from tags.models import Tag


class Book (models.Model):
    title=models.CharField("Название",max_length=64)
    date=models.DateField("Дата публикации")
    short_description=models.TextField("Краткое описание",max_length=256,blank=True, null=True, default=None)
    image = models.ImageField(upload_to='books_images/',blank=True, null=True, default=None)
    authors=models.ForeignKey(Author)
    tags=models.ManyToManyField(Tag,related_name="tags",related_query_name="tags")

    def __str__(self):
        return "%s" % self.title

    class Meta:

        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'




