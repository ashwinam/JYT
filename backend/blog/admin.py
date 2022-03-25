from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Post)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(models.BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass