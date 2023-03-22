from fpdf import FPDF

page_header_names = ["Start page", "Middle page", "Last page"]
page_footer_name = ["1", "2", "3"]

pdf = FPDF(orientation="P", unit="mm", format="A4") # P - portrait
pdf.set_auto_page_break(auto=False, margin=0)

for page_header, page_footer in zip(page_header_names, page_footer_name):
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=page_header, align="L", ln=1) #border=1 to see cell
    pdf.line(10, 21, 200, 21)
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=page_footer, align="R")

pdf.output("output.pdf")




