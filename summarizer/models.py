from django.db import models

# Create your models here.
class PDFDocument(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pdf_file.name