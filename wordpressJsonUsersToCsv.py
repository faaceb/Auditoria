#!/usr/bin/python

##################################################################################
# Script para converter arquivos JSON contendo os usuarios do Wordpress para CSV #
##################################################################################

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
campos = ['arquivo_json', 'ID', 'login', 'email', 'name', 'first_name', 'last_name', 'nice_name', 'URL', 'avatar_URL', 'profile_URL', 'ip_address', 'site_id', 'roles', 'is_super_admin']
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
    caminhoArquivoCSVAberto.write('%s%s%s%s' % (caractTerminador, campoRole, caractTerminador, caractSeparador))
    caminhoArquivoCSVAberto.write('\n') #Pular uma linha

#Contador utilizado no Loop principal
contador = 1

#Executa a extracao em cada arquivo JSON contido no Diretorio
for arq in os.listdir(diretorio):
    arqCaminhoCompleto = '%s\%s' % (diretorio, arq)

    #Abertura de cada arquivo JSON e Parse
    with open(arqCaminhoCompleto, 'r') as arquivoJSON:
        f = demjson.decode(arquivoJSON.read())
    
    #--------------------------------------#
    # Coleta dos dados  e construcao do CSV#
    #--------------------------------------#

    #Coleta dos dados JSON
    for users in f.get('users'):
        
        #Apaga o conteudo da variavel
        linha = ''
        
        #Quantidade de roles do usuario
        for role in users.get('roles'):
        
            #Construcao da linha a partir da coleta dos dados do JSON
            for cadaCampo in campos:
                
                #Se o campo da vez for arquivo_json, retorna o nome do arquivo
                campoDaVez = cadaCampo
                if campoDaVez == 'arquivo_json':
                    campoDaVez = arq
                else:
                    campoDaVez = users.get(cadaCampo)
                    
                #Construcao da linha
                linha = '%s%s%s%s%s' % (linha, caractTerminador, campoDaVez, caractTerminador, caractSeparador)
                
            #Inclusao da role na linha
            linha = '%s%s%s%s%s' % (linha, caractTerminador, role, caractTerminador, caractSeparador)
            
            #Adiciona a linha de registro ao arquivo CSV
            with open(arquivoCSV, 'a+') as caminhoArquivoCSVAberto:
                linhaDecodificada = linha.encode("windows-1252")
                caminhoArquivoCSVAberto.write('%s' % (linhaDecodificada))
                caminhoArquivoCSVAberto.write('\n') #Pular uma linha

            #Apaga o conteudo da variavel
            linha = ''
        
    print('\n')
    print('%s: %s%s%s' % (contador, 'Arquivo: ', arq, ' - Processado.\n'))
    contador = contador + 1

print ('---PROCESSO FINALIZADO---')
