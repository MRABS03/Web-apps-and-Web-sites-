import pandas as pd
import glob
from fpdf import FPDF  

filepaths=glob.glob('invoices\*.xlsx')
print(filepaths)



for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    titles = filepath.strip('.xlsx')
    titles=titles.strip(fr"invoices\\")
    invoice_no, date = titles.split('-')

    #Adding Page
    pdf = FPDF(orientation='P', unit='mm', format='a4')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=16)
    #Adding header
    pdf.cell(w=0,h=16,border=0,ln=1,txt=f"Invoice nr.{invoice_no}")
    pdf.cell(w=0,h=16,border=0,ln=1,txt=f"Date {date}")
    #Adding columns name
    columns=df.columns
    columns=[item.replace("_"," ").title() for item in columns]
    pdf.cell(w=28, h=8, border=1, txt=str(columns[0].title()))
    pdf.cell(w=48, h=8, border=1, txt=str(columns[1].title()))
    pdf.cell(w=48, h=8, border=1, txt=str(columns[2].title()))
    pdf.cell(w=40, h=8, border=1, txt=str(columns[3].title()))
    pdf.cell(w=30, h=8, border=1, txt=str(columns[4].title()), ln=1)

    for index,row in df.iterrows():

        pdf.set_font(family='Times',size=12)
        pdf.cell(w=28,h=8,border=1,txt=str(row['product_id']))
        pdf.cell(w=48,h=8,border=1,txt=str(row['product_name']))
        pdf.cell(w=48,h=8,border=1,txt=str(row['amount_purchased']))
        pdf.cell(w=40,h=8,border=1,txt=str(row['price_per_unit']))
        pdf.cell(w=30,h=8,border=1,txt=str(row['total_price']),ln=1)

    total=str(df['total_price'].sum())
    pdf.cell(w=28, h=8, border=1, txt='')
    pdf.cell(w=48, h=8, border=1, txt='')
    pdf.cell(w=48, h=8, border=1, txt='')
    pdf.cell(w=40, h=8, border=1, txt='')
    pdf.cell(w=30, h=8, border=1, txt=str(total),ln=1)

    #ADDing company name
    pdf.set_font(family='Times', size=12,style='B')
    pdf.cell(w=30, h=8, border=0, txt=f"Your total is {total}",ln=1)
    pdf.cell(w=25, h=8, border=0, txt=f"PythonHow")
    pdf.image("pythonhow.png",w=10)

    pdf.output(fr"pdfs\{invoice_no}.pdf")



