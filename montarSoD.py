# -*- coding: iso-8859-1 -*-

#Arquivo contendo as funcoes e respectivas transacoes
matrizConflitos = "matrizConflitosLibbs.csv"
#matrizConflitos = "matrizConflitos.csv"
#matrizConflitos = "matrizConflitosInternet.csv"
#matrizConflitos = "matrizConflitosInternet2.csv"
transacoes = "transacoes.csv"

#Listas e dicionarios
tcodes = []
listFuncTcodes = []
tcodesCombinados = []
dicionario = {}

#Abre o arquivo de conflitos e inclui em uma lista
with open(matrizConflitos, 'r') as arq1:
    for rows in arq1:
        chave = "%s;%s" % (rows.split(';')[1].replace('\r','').replace('\n',''),rows.split(';')[2].replace('\r','').replace('\n',''))
        valor = "%s" % (rows.split(';')[3].replace('\r','').replace('\n',''))
        dicionario[chave] = valor

#Abre o arquivo de transacoes, executa a combinacao e inclui em uma lista
with open(transacoes, 'r') as arq2:
    for linha in arq2:
        tcodes.append(linha.replace('\r','').replace('\n',''))
    for i in tcodes:
        for x in tcodes:
            if i != x:
                tcodesCombinados.append('%s;%s' % (i,x))

#print (dicionario['VA32;VE88'])

def verificaConflito(transacaoCombinada):
    if dicionario.get(transacaoCombinada, False):
        return True
    else:
        return False

for cadaTcode in tcodesCombinados:
    if verificaConflito(cadaTcode) == True:
        print('%s;%s' % (cadaTcode,dicionario.get(cadaTcode)))

print('--- FIM DO ARQUIVO ---\r\n')
