# -*- coding: latin-1 -*-

#Importa as classes necess�rias
import os

#Caminho onde os arquivos encontram-se
caminho = 'D:\Temp\SVP\PGMS\\'
todosOsArquivos = os.listdir(caminho)

#Palavra a ser pesquisada dentro dos arquivos
palavraPesquisada = 'SENHA'

#Abre o arquivo do resultado em memória
resultadoArquivo = open("resultado.txt", 'a')
resultadoArquivo.write("Palavra pesquisada: " + palavraPesquisada + "\n\n")
resultadoArquivo.write('{0: <30} {1: <10} {2}'.format("ARQUIVO","POSICAO","TRECHO") + "\n")

#Para cada arquivo que existe dentro do caminho, executa um bloco de instru��es
for file in todosOsArquivos:
     
    #Caminho completo de cada arquivo
    arquivo = caminho + str(file)
    
    #Abre o arquivo em modo bin�rio e converte os dados para Latin-1 mais legiveis
    f = open(arquivo, 'rb').read().decode('latin-1')
    pesquisa = f.find(palavraPesquisada)
    if (pesquisa > 0):
        trecho = str(f[pesquisa:pesquisa+100].replace("\n", " PulaLinha "))
        print('{0: <30} {1: <10} {2}'.format(file,pesquisa,trecho))
        resultadoArquivo.write('{0: <30} {1: <10} {2}'.format(file,pesquisa,str(bytes(trecho,"Latin-1")) + "\n"))

resultadoArquivo.write("\n\n")
resultadoArquivo.close()