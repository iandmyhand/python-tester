# fpdf2.     2.7.3
# PyPDF2     3.0.1
# reportlab  3.6.12

from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)
can.drawString(10, 100, "Sample Text.")
can.save()
packet.seek(0)

new_pdf = PdfReader(packet)
