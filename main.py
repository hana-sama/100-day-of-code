from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path
from PIL import Image
WIDTH = 210
HEIGHT = 297

class PDF(FPDF):
    def header(self):
        # Add logo
        self.image('./images/logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Invoice', 1, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

path = './invoices/'
all_files = glob.glob(path + '/*.xlsx')

for filepath in all_files:
    df = pd.read_excel(filepath)
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")
    total_sum = 0
    for index, row in df.iterrows():
        total_sum += row['total_price']


        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Times', '', 12)
        pdf.cell(0, 10, 'Sales Data', 0, 1)
        pdf.cell(0, 10, '-------------------------', 0, 1)

        # Add Invoice number and date
        pdf.set_font("Arial", "B", 12)
        pdf.cell(w=0, h=10, txt=f"Invoice nr: {invoice_nr[0]}")
        pdf.ln()
        pdf.cell(w=0, h=10, txt=f"Date: {invoice_nr[1]}")
        pdf.ln()
        
        # Add table
        pdf.set_font('Times', 'B', 12)
        pdf.cell(35, 10, 'Product ID', 1)
        pdf.cell(50, 10, 'Product Name', 1)
        pdf.cell(35, 10, 'Amount', 1)
        pdf.cell(35, 10, 'Price per Unit', 1)
        pdf.cell(35, 10, 'Total Price', 1)
        pdf.ln()

        for index, row in df.iterrows():
            pdf.set_font("Times", "", 12)
            pdf.cell(35, 10, str(row['product_id']), 1)
            pdf.cell(50, 10, row['product_name'], 1)
            pdf.cell(35, 10, str(row['amount_purchased']), 1)
            pdf.cell(35, 10, "$" + str(row['price_per_unit']), 1)
            pdf.cell(35, 10, "$" + str(row['total_price']), 1)
            pdf.ln()
        pdf.cell(35, 10, "Grand Total", 1)
        pdf.cell(50, 10, "", 1)
        pdf.cell(35, 10, "", 1)
        pdf.cell(35, 10, "", 1)
        pdf.cell(35, 10, f"${total_sum}", 1)
        pdf.ln()
        pdf.ln()
        pdf.set_font("Times", "B", 12)
        pdf.cell(30, 10, f"The total due amount is ${total_sum}.")
        pdf.ln()
        pdf.set_font("Times", "B", 14)
        pdf.cell(25, 10, f"True Axis")
        pdf.image('./images/logo.png', w=10)
        pdf.output(f'PDFs/invoice_for_{filename}.pdf', 'F')
        