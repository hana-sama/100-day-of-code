from fpdf import FPDF
import glob
from pathlib import Path
import re

class PDF(FPDF):
    def header(self):
        # Add logo
        self.image('./images/logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(50, 10, 'Classified Document', 0, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

path = './text_files/'
all_files = glob.glob(path + '/*.txt')

pdf = PDF()
for filepath in all_files:
    filename = Path(filepath).stem
    if filepath.endswith(".txt"):
        pdf.alias_nb_pages()
        pdf.add_page()

        # Set the font and font size
        pdf.set_font('Arial', '', size=12)
        pdf.cell(0, 10, '', 0,  1)
        pdf.cell(0, 10, '-------------------------', 0, 1)
        with open(filepath, 'r') as file:
            content = file.read()

            content = re.sub(r'\([^()]*\)|\[[^\[\]]*\]', '', content)


        # Write the text to the PDF
            pdf.set_font("Arial", 'B', size=15)
            pdf.cell(0, 5, f'{filename.title()}')
            pdf.ln()
            pdf.ln()
            pdf.set_font('Arial', '', size=12)
            pdf.multi_cell(0, 5, content)

# Save the PDF
pdf.output(f'PDFs/output.pdf', 'F')