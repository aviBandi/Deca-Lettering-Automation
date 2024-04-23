from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io
import os
import time


club_name = "Wayzata Track"
school_year = "2024-2025"



output_folder = "letteringPDFs"

# Reads in names from text file
with open("names", "r") as f:
    names = [line.strip() for line in f]

start_time = time.time()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def greet():
    print("hello world")

def add_words_to_pdf(input_pdf_path, output_pdf_path, name, center_point):
    fontSize = 30
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Register the custom gothic font
    custom_gothic_font_path = "data/gothicText.ttf"  # Replace with the path to your gothic font file
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

        # Translate canvas to the center of the text
        can.translate(x + text_width / 2, y + text_height / 2)

        # Draw the text
        can.rotate(90)  # Rotate the canvas by 90 degrees
        can.drawString(-text_width / 2, -text_height / 2, name)  # Draw text at (-text_width / 2, -text_height / 2) after rotation
        can.save()

        packet.seek(0)
        new_page = PdfReader(packet)
        page.merge_page(new_page.pages[0])
        writer.add_page(page)

    with open(os.path.join(output_folder, output_pdf_path), "wb") as f:
        writer.write(f)






if __name__ == "__main__":
    for each in names:
        add_words_to_pdf("data/letteringDoc.pdf", each.split()[-1] + each.split()[0] + "Lettering" + ".pdf", each, (285, 540))
        add_words_to_pdf(os.path.join(output_folder,each.split()[-1]+each.split()[0])+"Lettering"+".pdf", each.split()[-1]+each.split()[0]+"Lettering"+".pdf", club_name, (373, 540))
        add_words_to_pdf(os.path.join(output_folder,each.split()[-1]+each.split()[0])+"Lettering"+".pdf", each.split()[-1]+each.split()[0]+"Lettering"+".pdf", school_year, (430, 540))
        print("Letter created for: ", each)

    end_time = time.time()
    print("\n")
    print(f"{len(names)} Letters created successfully in {end_time - start_time} seconds.")