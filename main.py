from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    topic = row["Topic"]
    num_of_pages = row["Pages"]
    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)
    pdf.ln(265)
    # Set footer
    pdf.set_font('Arial', 'I', 8)
    # Set text color
    pdf.set_text_color(180, 180, 180)
    # Print centered page number
    pdf.cell(w=0, h=10, txt=topic, align='C')

    for i in range(num_of_pages - 1):
        pdf.add_page()
        for y in range(20, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)
        # Set footer
        pdf.ln(277)
        pdf.set_font('Arial', 'I', 8)
        # Set text color
        pdf.set_text_color(180, 180, 180)
        # Print centered page number
        pdf.cell(w=0, h=10, txt=topic, align='C')


pdf.output("output.pdf")