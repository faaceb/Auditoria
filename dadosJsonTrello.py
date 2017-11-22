#!/usr/bin/python

###################################################
# Script para extrair dados do JSON do app Trello #
###################################################

#Importa as bibliotecas necessarias
import os
import demjson

#Diretorio onde encontram-se os arquivos JSON
diretorio = 'C:\\Users\\a37117\\Desktop\\JSON_Files'

#Arquivo CSV resultante
arquivoCSV = 'resultadoExtracaoJSON.csv'

#Caracteres de separacao do CSV
caractTerminador = '"'
caractSeparador = ','

#Campos
campos = ['arquivo_json', 'ID', 'Name']
campoRole = 'role'

#Cabecalho do CSV
cabecalho = ''
for cadaCampo in campos:
    if cabecalho == '':
        cabecalho = '%s%s%s%s' % (caractTerminador, cadaCampo, caractTerminador, caractSeparador)
    else:
        cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, cadaCampo, caractTerminador, caractSeparador)

#Cria o Arquivo CSV e adiciona o cabecalho (campos)
with open(arquivoCSV, 'w+') as caminhoArquivoCSVAberto:
    caminhoArquivoCSVAberto.write(cabecalho)
    caminhoArquivoCSVAberto.write('%s%s%s' % (caractTerminador, caractTerminador, caractSeparador))
    caminhoArquivoCSVAberto.write('\n') #Pular uma linha

#Contador utilizado no Loop principal
contador = 1

for arq in os.listdir(diretorio):
    arqCaminhoCompleto = '%s\%s' % (diretorio, arq)

    #Abertura de cada arquivo JSON e Parse
    with open(arqCaminhoCompleto, 'r') as arquivoJSON:
        f = demjson.decode(arquivoJSON.read())
    
    #--------------------------------------#
    # Coleta dos dados  e construcao do CSV#
    #--------------------------------------#

    acoes = {}

    for actions in f.get('actions'):
    
        if unicode(actions.get('data', {}).get('listAfter', {}).get('name')) == 'DONE':
            conteudo = {unicode(actions.get('data', {}).get('card', {}).get('idShort')) : actions.get('date')}
            acoes.update(conteudo)
    
    #Coleta dos dados JSON
    for cards in f.get('cards'):

        #Apaga o conteudo da variavel
        linha = ''
        
        #Inlcui o nome do arquivo na linha
        linha = '%s%s%s%s' % (caractTerminador, arq, caractTerminador, caractSeparador)
        
        #Coletando dados
        name = cards.get("name")
        linha = '%s%s%s%s%s' % (linha, caractTerminador, name, caractTerminador, caractSeparador)
        
        url = cards.get("url")
        linha = '%s%s%s%s%s' % (linha, caractTerminador, url, caractTerminador, caractSeparador)
        
        for acaoId, dataAcao in acoes.items():
         
            #print '%s : %s' % (cards.get("idShort"), acaoId)
            
            if str(cards.get("idShort")) == str(acaoId):
                linha = '%s%s%s%s%s' % (linha, caractTerminador, dataAcao, caractTerminador, caractSeparador)
                break
        
        print linha

    print('\n')
    print('%s: %s%s%s' % (contador, 'Arquivo: ', arq, ' - Processado.\n'))
    contador = contador + 1

print ('---PROCESSO FINALIZADO---')
