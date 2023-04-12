import io
import os
import reportlab.rl_config
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader

ORIGINAL_FILENAME = "invoice.pdf"
DESTINATION_FILENAME = "destination.pdf"

if os.path.exists(DESTINATION_FILENAME):
  os.remove(DESTINATION_FILENAME)
  print(f"The file {DESTINATION_FILENAME} has been deleted successfully")

reportlab.rl_config.warnOnMissingFontGlyphs = 0

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)
can.setFont('Vera', 6)

can.drawString(100, 300, f"MILANO, IT")
can.drawString(200, 300, f"INCHEON, KR")
can.save()
packet.seek(0)

new_pdf = PdfReader(packet)
existing_pdf = PdfReader(open(ORIGINAL_FILENAME, "rb"))
output = PdfWriter()
page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)
output_stream = open(DESTINATION_FILENAME, "wb")
output.write(output_stream)
output_stream.close()
print(f"{DESTINATION_FILENAME} created.")
