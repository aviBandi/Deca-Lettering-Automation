# Works with a custom font but does not center

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io

def add_names_to_pdf(input_pdf_path, output_pdf_path, name, coordinates):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Register the custom gothic font
    custom_gothic_font_path = "gothicText.ttf"  # Replace with the path to your gothic font file
    pdfmetrics.registerFont(TTFont('Gothic', custom_gothic_font_path))

    for page in reader.pages:
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Set typography options
        can.setFont("Gothic", 75)  # Set custom gothic font family and size
        can.setFillColor(colors.black)  # Set text color

        x, y = coordinates
        can.drawString(x, y, name)

        can.save()

        packet.seek(0)
        new_page = PdfReader(packet)
        page.merge_page(new_page.pages[0])
        writer.add_page(page)

    with open(output_pdf_path, "wb") as f:
        writer.write(f)


# Example usage
input_pdf_path = "blankDoc.pdf"
output_pdf_path = "output.pdf"
name = 'Avi Bandi'
coordinates = (250, 600)
add_names_to_pdf(input_pdf_path, output_pdf_path, name, coordinates)
print("done")