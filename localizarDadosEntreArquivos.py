# -*- coding: latin-1 -*-

#Arquivo contendo as palavras a serem pesquisadas
arquivoPalavras = 'arquivoPalavras.txt'

#Arquivo contendo o texto a ser pesquisado
arquivoTexto = 'arquivoTexto.txt'

#Lista utilizada para conter as palavras a serem pesquisadas
palavras = []

#Contador
contador = 1

with open(arquivoPalavras, 'r') as f:
    for linha in f:
        palavras.append(linha.replace('\n','').lower())

with open(arquivoTexto, 'r') as f:
    for palavra in palavras:
        #palavraEncontrada = 'N'
        for linhasTexto in f:
            busca = linhasTexto.lower().find(palavra)
            if busca != -1:
                if busca - 10 < 0:
                    trechoInicio = 0
                else:
                    trechoInicio = busca - 10
                if busca + 20 > len(linhasTexto):
                    trechoFim = len(linhasTexto) - 1
                else:
                    trechoFim = busca + 20
                trecho = linhasTexto[trechoInicio:trechoFim]
                print('String: \"%s\": encontrada na linha: %s --- Trecho: %s' % (palavra, contador, trecho))
                palavraEncontrada = 'S'
            contador = contador + 1
        #if palavraEncontrada == 'N':
        #    print('String: \"%s\":' % (palavra)) 
        f.seek(0, 0)
        contador = 1
