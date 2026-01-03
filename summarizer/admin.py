from django.contrib import admin
from .models import PDFDocument

@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('pdf_file', 'uploaded_at')
    readonly_fields = ('uploaded_at',)
