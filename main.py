# Works with custom font and centers around the center value specified.

names = ['Avi Bandi', 'Varun Nagapakar', 'Sai Kimbler']

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io

def add_words_to_pdf(input_pdf_path, output_pdf_path, name, center_point):
    fontSize = 30
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Register the custom gothic font
    custom_gothic_font_path = "gothicText.ttf"  # Replace with the path to your gothic font file
    pdfmetrics.registerFont(TTFont('Gothic', custom_gothic_font_path))

    for page in reader.pages:
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Set typography options
        can.setFont("Gothic", fontSize)  # Set custom gothic font family and size
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
# input_pdf_path = "blankDoc.pdf"
# output_pdf_path = "output3.pdf"
# name = 'Avi Bandi'
# center_point = (310, 600)  # Example center point coordinates
# add_words_to_pdf(input_pdf_path, output_pdf_path, name, center_point)
# print("Done")
# add_words_to_pdf("output3.pdf", "output3.pdf", "Varun Nagapakar", (310, 300))
# print("done")

for each in names:
    add_words_to_pdf("blankDoc.pdf", each.split()[1]+each.split()[0]+"Lettering"+".pdf", each, (310, 600))
    add_words_to_pdf(each.split()[1]+each.split()[0]+"Lettering"+".pdf", each.split()[1]+each.split()[0]+"Lettering"+".pdf", "Wayzata DECA", (310, 300))

    print("done")