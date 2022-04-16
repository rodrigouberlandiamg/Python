import os
from PyPDF2 import PdfFileWriter, PdfFileReader

def extract_page(doc_name, page_num):
    pdf_reader = PdfFileReader(open(doc_name, 'rb'))
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(page_num))
    with open(f'document-page{page_num}.pdf', 'wb') as doc_file:
        pdf_writer.write(doc_file)

pasta = 'C:\Fontes\public\python\Alura\pdf_paginas\DISPENSA SEM JUSTA CAUSA - UAI PAMPULHA'
for i in range(0,15):
    # with open(f'C:\Fontes\public\python\Alura\pdf_paginas\DISPENSA SEM JUSTA CAUSA - UBS PAMPULHA\document-page{i}.pdf','r') as pdf_file:
    pdf_file = f'{pasta}\document-page{i}.pdf'
    # for x in range(0,2):
    #     extract_page(pdf_file,x)
    #Faz a leitura usando a biblioteca
    read_pdf = PdfFileReader(pdf_file)
    # pega o numero de páginas
    number_of_pages = read_pdf.getNumPages()
    #lê a primeira página completa
    page = read_pdf.getPage(0)
    #extrai apenas o texto
    page_content = page.extractText()
    print(page_content)
    pos_ini = page_content.find('Sr(a):')
    pos_final = page_content.find('/')
    nome = page_content[pos_ini+6:pos_final]
    print(nome)
    os.rename(f'{pasta}\document-page{i}.pdf',f'{pasta}\{nome}.pdf')