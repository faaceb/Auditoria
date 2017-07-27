# -*- coding: utf-8 -*-
###########################################################################
# Script para descobrir diretorios em websites (parecido com o DirBuster) #
###########################################################################

#Bibliotecas necessarias
import requests

#URL Destino
url = 'http://www.airticketbook.in'

#Arquivo que contem o dicionario de diretorios
arquivo = 'diretorios.txt'
with open(arquivo) as arquivoAberto:
    linhas = arquivoAberto.read().splitlines()

#Imprime cabecalho
print ('URL;STATUS_CODE\n')

#contador
contador = 0

#Para cada linha no arquivo, execute
for cadaLinha in linhas:
    
    #Acessa a URL
    urlCompleta = url + cadaLinha
    r = requests.head(urlCompleta)
    
    contador = contador + 1
    
    #Imprime o resultado do acesso
    resultadoLinha = ('%s;%s;%s' % (contador,urlCompleta, r.status_code))
    print (resultadoLinha)
    
    #Arquivo que contem o resultado da analise
    arquivo = 'resultado.txt'
    with open(arquivo, 'a+') as arquivoAberto:
        arquivoAberto.write(resultadoLinha + '\n')
