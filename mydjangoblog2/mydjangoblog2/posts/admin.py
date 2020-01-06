# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data"]
    list_filter = ["data"]
    search_fields = ["titolo", "contenuto"]
    prepopulated_fields = {"slug": ("titolo",)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)       