from django.contrib import admin

from .models import Document, Text


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    ...


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    ...
