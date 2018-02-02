from django.contrib import admin
from .models import *



class TagAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]

    class Meta:
        model = Tag

admin.site.register(Tag, TagAdmin)