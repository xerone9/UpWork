import xml.etree.ElementTree as ET
import barcode
from barcode.writer import ImageWriter
from fpdf import FPDF
from PyPDF2 import PdfMerger

tree = ET.parse('PLUs.xml')
root = tree.getroot()

products = []
prices = []
upcs = []
pdfs = []

for item in root.iter('description'):
    products.append(item.text)

for item in root.iter('price'):
    prices.append(item.text)

for item in root.iter('upc'):
    upcs.append(item.text)

product_price = {}

for product, price, upc in zip(products, prices, upcs):
    product_price.update({product: [upc, price]})

for key in product_price:
    for values in product_price[key]:
        name = key
        code = product_price[key][0]
        amount = product_price[key][1]

        sample_barcode = barcode.get('code39', code, writer=ImageWriter())
        generated_filename = sample_barcode.save('00000000020015')

        pdf = FPDF('L', 'mm', (55, 100))
        pdf.add_page()
        pdf.set_font('Courier', '', 18)
        pdf.multi_cell(80, 6, name, align='C')
        if len(name) <= 19:
            pdf.ln(17)
        else:
            pdf.ln(11)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(10, 1, '$' + amount, align='L', ln=0)
        pdf.cell(1)
        pdf.image('00000000020015.png', 40, 25, 55)
        pdf.output('tuco/' + code + '.pdf', 'F')
        pdfs.append('tuco/' + code + '.pdf')

merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)

merger.write("tuco/all_tags.pdf")
merger.close()







