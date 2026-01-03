import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text
    
def generate_summary(text, max_sentences=5):
    import re
    # Split on sentence-ending punctuation, keep sentences concise
    sentences = re.split(r'(?<=[.!?])\s+', text.strip()) if text else []
    points = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        # Remove trailing punctuation for cleaner bullets
        s = s.rstrip('\n\r\t ')
        points.append(s)
        if len(points) >= max_sentences:
            break
    return points