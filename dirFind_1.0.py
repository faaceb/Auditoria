# -*- coding: utf-8 -*-
###########################################################################
# Script para descobrir diretorios em websites (parecido com o DirBuster) #
###########################################################################

#Bibliotecas necessarias
import requests

#URL Destino
url = 'http://www.airticketbook.in'

#Arquivo que contem o dicionario de diretorios
arquivo = 'Dirs1.txt'
with open(arquivo) as arquivoAberto:
    linhas = arquivoAberto.read().splitlines()

#Imprime cabecalho
print ('URL;STATUS_CODE\n')

#Para cada linha no arquivo, execute
for cadaLinha in linhas:

    #Acessa a URL
    urlCompleta = url + cadaLinha
    r = requests.head(urlCompleta)

    #Imprime o resultado do acesso
    print ('%s;%s' % (urlCompleta, r.status_code))
