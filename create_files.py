import pandas as pd
import subprocess
from PyPDF2 import PdfWriter

def sh(comando):
    subprocess.run(comando, shell=True)

passwds = pd.read_csv('passwd.csv',header=0)
list_pass = list(passwds)

#create zip files
for i, password in enumerate(list_pass):
    arquivo = f'arquivoszip/arquivo{i+1}'
    with open(arquivo,'w') as f:
        f.write('ABC')
    sh(f'touch {arquivo} && 7z a -p{password} {arquivo}.zip {arquivo} && rm -rf {arquivo}')

#create pdf files
for i, password in enumerate(list_pass):
    pdf = PdfWriter()
    pdf.encrypt(password)
    name = f'arquivospdf/pdf{i+1}.pdf'
    with open(name, 'wb') as e:
        pdf.write(e)