# -*- coding: iso-8859-1 -*-

print('--- INICIO DO PROCESSAMENTO ---\r\n')

#imports
import requests
from datetime import datetime
import zipfile

#Dicionarios
dicionario = []
cnpj = []
resultados = []

#Obtem data atual
now = datetime.now()
ano = now.year
if now.month <= 9:
    mes = "%s%s" % ("0",now.month)
else:
    mes = now.month
dia = now.day

#URL ANALISADAS
url = {}
urlInidoneos = "http://arquivos.portaldatransparencia.gov.br/downloads.asp?a=%s&m=%s&d=%s&consulta=ceis" % (ano,mes,dia)
url = {"inidoneos": urlInidoneos}

#Abre arquivo de CNPJ e inclui em uma lista
arqCnpj = "cnpj.csv"
with open(arqCnpj, 'r') as arq1:
    for rows in arq1:
        cnpj.append(rows.replace('\r','').replace('\n',''))

#Acessa URL
response = requests.get(url["inidoneos"], allow_redirects=True)

#Download do arquivo de Inidoneos
arqInidoneos = "inidoneos.zip"
with open(arqInidoneos, 'wb') as arq1:
    arq1.write(response.content)

#Descompacta o arquivo recebido do Portal da Transparencia
zip_ref = zipfile.ZipFile(arqInidoneos, 'r')
zip_ref.extractall()
zip_ref.close()

#Abre o arquivo de inidoneos e inclui em uma lista
arqInidoneosCsv = "%s%s%s_CEIS.csv" % (ano,mes,dia)
with open(arqInidoneosCsv, 'r', encoding="iso-8859-1") as arq1:
    for rows in arq1:
        dicionario.append(rows.replace('"',""))

#Pesquisa os CNPJ na lista de Inidoneos e retorna os resultados
cabecalho = False
for cadaCnpj in cnpj:
    for cadaRegistro in dicionario:
        cnpjDoRegistro = cadaRegistro.split(";")[1]
        if cadaCnpj == cnpjDoRegistro:
            resultados.append(cadaRegistro)
            print(cadaRegistro)

#Armazena os resultados em um arquivo CSV
arqResultado = "arqResultado.csv"
with open(arqResultado, 'w', encoding="iso-8859-1") as arq1:
    arq1.write(dicionario[0])
    for rows in resultados:
        arq1.write(rows)

#Informa resultado final ao usuario
qtdResultados = len(resultados)
print("Foram identificados %s registro(s)\r\n" % (qtdResultados))
print('--- FIM DO PROCESSAMENTO ---\r\n')