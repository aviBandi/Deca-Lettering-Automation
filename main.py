# Works with custom font and centers around the center value specified.

names = ['Avi Bandi', 'Varun Nagapakar', 'Sai Kimbler', "Rahul Billakanti", "Paul Kimbler", "Avinash Bandi",
         "Lexi Shasher", "Michelle Jacklitch", "Michael Lindsay", "Rowan Huh", "Aman Syaed", "Cole Paul Ledman",
         "Prohitt Ram Kumar", "Scott Gengler", "Brooks Gengler", "Kavin Gunnalseeland", "Viswas Valla",
         "Rukshan Rajan", "Dilshan Rajan", "Jack Berge", "Daniel Salantino", "Aaron Beduhn", "Tika Kude",
         "Jacklitch Kude", "Fan Boy" "Liam Hall", "Drew Nepsted", "Will Weber", "Amogh Rajgopal", "Maddy Vickers",
         "Robyn Van Horn", "Pranav Gangireddy", "Nithya Dharmagari", "Ashwanth Vishwanathan", "Ruan Paunland",
         "Michael Shumaker"]

print("Letters to generate:", len(names))

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

        # Draw the text
        can.drawString(x, y, name)
        can.save()

        packet.seek(0)
        new_page = PdfReader(packet)
        page.merge_page(new_page.pages[0])
        writer.add_page(page)

    with open(os.path.join(output_folder, output_pdf_path), "wb") as f:
        writer.write(f)

for each in names:
    add_words_to_pdf("data/letteringDoc.pdf", each.split()[-1] + each.split()[0] + "Lettering" + ".pdf", each, (310, 600))
    add_words_to_pdf(os.path.join(output_folder,each.split()[-1]+each.split()[0])+"Lettering"+".pdf", each.split()[-1]+each.split()[0]+"Lettering"+".pdf", "Wayzata DECA", (310, 300))
    print("Letter created for: ", each)



end_time = time.time()
print("\n")
print("Execution time: ", end_time-start_time, "Seconds")
