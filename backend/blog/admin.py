from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Post)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title']
