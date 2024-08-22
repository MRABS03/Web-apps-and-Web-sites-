from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P',unit='mm',format='a4')
pdf.set_auto_page_break(auto=False)
df=pd.read_csv('topicspdf.csv')

hol=10
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',size=12,style='B')
    pdf.cell(w=0,h=12,align='L',border=0,ln=1,txt=row['Topic'])
    #pdf.line(10,21,200,21)
    for i in range(1,28):
        x=(12+i*hol)
        pdf.line(10,x,200,x)

    pdf.ln(265)
    pdf.set_font(family='Times',size=8,style='I')
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,align='R',txt=f"{row['Topic']}")

    for page in range(row['Pages']-1):
        pdf.add_page()
        for i in range(1, 28):
            x=(12 + i * hol)
            pdf.line(10,x,200,x)
        pdf.ln(277)
        pdf.set_font(family='Times', size=8, style='I')
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, align='R', txt=f"{row['Topic']}")

pdf.output('output.pdf')