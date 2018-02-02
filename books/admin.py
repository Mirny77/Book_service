from django.contrib import admin
from .models import *



class BookAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]

    class Meta:
        model = Book

admin.site.register(Book, BookAdmin)