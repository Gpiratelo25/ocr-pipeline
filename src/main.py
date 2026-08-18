import pymupdf
import re



caminho = r'ocr-pipeline\data\raw\mcc-export-44a181c3-a47f-4ca2-b53c-df30c9f8f728\archive\documents\18672\000108981909000016\exhibit103.pdf'
caminho2=r'C:\Users\MICRO\OneDrive\Documents\Projetos\ocr-pipeline\data\raw\mcc-export-44a181c3-a47f-4ca2-b53c-df30c9f8f728\archive\documents\21076\000002107604000094\ex10-4.pdf'
caminho3=r'ocr-pipeline\data\raw\mcc-export-44a181c3-a47f-4ca2-b53c-df30c9f8f728\archive\documents\32258\000003225802000065\sl_murrayst.pdf'
doc=pymupdf.open(caminho3)

with open(r'ocr-pipeline\data\new1\archive\documents\8947\000093066102001852\dex1025.txt','r') as file:
        paginas=file.readlines()
        # linhas = [linha.strip() for linha in texto_original.splitlines()]

    # Remove linhas vazias
        linhas = [linha for linha in paginas if linha]

        texto = "\n".join(linhas)



# total_paginas=len(doc)



# texto_original = "\n".join (page.get_text() for page in doc)
# padrao=r"as of ([A-Z][a-z]+\s+\d{1,2},\s+\d{4})"


# linhas = [linha.strip() for linha in texto_original.splitlines()]

# # Remove linhas vazias
# linhas = [linha for linha in linhas if linha]

# texto = "\n".join(linhas)

# # Remove espaços duplicados
# texto = re.sub(r"[ \t]+", " ", texto)
# dates=re.findall(padrao,texto, re.IGNORECASE)


# doc.close()
# print(texto[:4500])










print(texto[:4500])
