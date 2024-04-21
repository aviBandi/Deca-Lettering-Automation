


names = ['Avi Bandi', 'Varun Nagapakar', 'Sai Kimbler', "Rahul Billakanti", "Paul Kimbler", "Avinash Bandi",
         "Lexi Shasher", "Michelle Jacklitch", "Michael Lindsay", "Rowan Huh", "Aman Syaed", "Cole Paul Ledman",
         "Prohitt Ram Kumar", "Scott Gengler", "Brooks Gengler", "Kavin Gunnalseeland", "Viswas Valla",
         "Rukshan Rajan", "Dilshan Rajan", "Jack Berge", "Daniel Salantino", "Aaron Beduhn", "Tika Kude",
         "Jacklitch Kude", "Fan Boy" "Liam Hall", "Drew Nepsted", "Will Weber", "Amogh Rajgopal", "Maddy Vickers",
         "Robyn Van Horn", "Pranav Gangireddy", "Nithya Dharmagari", "Ashwanth Vishwanathan", "Ruan Paunland",
         "Michael Shumaker"]


from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import io
import os
import time


start_time = time.time()

output_folder = "letteringPDFs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

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



for each in names:
    add_words_to_pdf("data/letteringDoc.pdf", each.split()[-1] + each.split()[0] + "Lettering" + ".pdf", each, (285, 540))
    add_words_to_pdf(os.path.join(output_folder,each.split()[-1]+each.split()[0])+"Lettering"+".pdf", each.split()[-1]+each.split()[0]+"Lettering"+".pdf", "Wayzata DECA", (373, 540))
    add_words_to_pdf(os.path.join(output_folder,each.split()[-1]+each.split()[0])+"Lettering"+".pdf", each.split()[-1]+each.split()[0]+"Lettering"+".pdf", "2023-2024", (430, 540))
    print("Letter created for: ", each)



end_time = time.time()
print("\n")
print(f"{len(names)} Letters created successfully in {end_time - start_time} seconds.")