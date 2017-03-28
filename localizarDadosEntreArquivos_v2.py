# -*- coding: utf-8 -*-

import codecs

#Arquivo contendo as palavras a serem pesquisadas
arquivoPalavras = 'arquivoPalavras.txt'

#Arquivo contendo o texto a ser pesquisado
arquivoTexto = 'svv.exe'

#Arquivo que sera gerado com o resultado da analise
arqResultado = 'svv.txt'

#Lista utilizada para conter as palavras a serem pesquisadas
palavras = []

#Quantidade de caracteres listados no trecho quando uma string é encontrada
qtdCaracteres = 30

#Contador
contador = 1

with codecs.open(arqResultado, 'w+', encoding='utf-8', errors='ignore') as resultado:
    resultado.write('--- INICIO DO ARQUIVO ---\r\n')

with codecs.open(arquivoPalavras, 'r', encoding='utf-8', errors='replace') as f:
    for linha in f:
        palavras.append(linha.replace('\r','').replace('\n','').lower())

with codecs.open(arquivoTexto, 'r', encoding='utf-8', errors='replace') as f:
    for palavra in palavras:
        #palavraEncontrada = 'N'
        for linhasTexto in f:
            linhasTexto = linhasTexto.lower()
            busca = linhasTexto.find(palavra)
            if busca != -1:
                if busca - qtdCaracteres < 0:
                    trechoInicio = 0
                else:
                    trechoInicio = busca - qtdCaracteres
                if busca + (qtdCaracteres * 2) > len(linhasTexto):
                    trechoFim = len(linhasTexto) - 1
                else:
                    trechoFim = busca + (qtdCaracteres * 2)
                trecho = linhasTexto[trechoInicio:trechoFim]
                with codecs.open(arqResultado, 'a+', encoding='utf-8', errors='ignore') as resultado:
                    resultado.write('String: \"%s\": encontrada --- Trecho: %s' % (palavra, trecho))
                    resultado.write('\r\n')
                print('String: \"%s\": encontrada --- Trecho: %s' % (palavra, trecho))
                #palavraEncontrada = 'S'
            contador = contador + 1
        #if palavraEncontrada == 'N':
        #    print('String: \"%s\":' % (palavra)) 
        f.seek(0, 0)
        contador = 1

with codecs.open(arqResultado, 'a+', encoding='utf-8', errors='ignore') as resultado:
    resultado.write('--- FIM DO ARQUIVO ---\r\n')
