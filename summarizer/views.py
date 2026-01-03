
from django.shortcuts import render, redirect, get_object_or_404
from .models import PDFDocument
from .utils import extract_text_from_pdf, generate_summary
import logging

logger = logging.getLogger(__name__)

def index(request):
    summary = None
    message = None
    latest_pdf = None

    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf = request.FILES['pdf']
        try:
            # Create model instance (file saved to MEDIA_ROOT)
            pdf_obj = PDFDocument.objects.create(pdf_file=pdf)

            # Extract text and generate summary points
            text = extract_text_from_pdf(pdf_obj.pdf_file.path)
            summary_points = generate_summary(text)

            # Save as newline-separated text for storage
            pdf_obj.summary = '\n'.join(summary_points)
            pdf_obj.save()

            # Redirect to detail page for the new PDF
            return redirect('pdf_detail', pk=pdf_obj.pk)
        except Exception as e:
            logger.exception("Error processing uploaded PDF")
            message = f"Error processing PDF: {e}"

    # If no new upload, show the most recent saved PDF (if any)
    if not latest_pdf:
        latest_pdf = PDFDocument.objects.last()

    latest_summary_points = None
    if latest_pdf and latest_pdf.summary:
        latest_summary_points = [line for line in latest_pdf.summary.splitlines() if line.strip()]

    return render(request, 'index.html', {'summary': summary, 'message': message, 'latest_pdf': latest_pdf, 'latest_summary_points': latest_summary_points})


def pdf_detail(request, pk):
    pdf_obj = get_object_or_404(PDFDocument, pk=pk)
    summary_points = [line for line in (pdf_obj.summary or '').splitlines() if line.strip()]
    return render(request, 'detail.html', {'pdf': pdf_obj, 'summary_points': summary_points})
