from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io

def add_names_to_pdf(input_pdf_path, output_pdf_path, names, coordinates):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Set typography options
        can.setFont("Times-Roman", 19)  # Set font family and size
        can.setFillColor(colors.black)  # Set text color

        x, y = coordinates
        for name in names:
            can.drawString(x, y, name)
            y -= 20  # Adjust spacing between names

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
names = ["Name1", "Name2", "Name3"]
coordinates = (250, 600)
add_names_to_pdf(input_pdf_path, output_pdf_path, names, coordinates)
