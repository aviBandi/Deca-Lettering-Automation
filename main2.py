from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io

def add_names_to_pdf(input_pdf_path, output_pdf_path, name, center_point):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    fontSize = 25
    for page in reader.pages:
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Set typography options
        can.setFont("Courier-Bold", fontSize)  # Set font family and size
        can.setFillColor(colors.black)  # Set text color

        # Calculate text width and height
        text_width = can.stringWidth(name)
        text_height = fontSize  # Font size in this case

        # Calculate starting coordinates for centering text
        x = center_point[0] - text_width / 2
        y = center_point[1] - text_height / 2

        # Draw the text
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
output_pdf_path = "output2.pdf"
name = 'Varun Nagapakar'
center_point = (300, 300)  # Example center point coordinates
add_names_to_pdf(input_pdf_path, output_pdf_path, name, center_point)

input_pdf_path = "blankDoc.pdf"
output_pdf_path = "output.pdf"
name = 'Varun'
center_point = (300, 400)  # Example center point coordinates
add_names_to_pdf(input_pdf_path, output_pdf_path, name, center_point)

# The text will be centered around the point (400, 400) on each page of the input PDF.