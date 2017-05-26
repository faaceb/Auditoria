# -*- coding: utf8 -*-
import win32com.client
from time import sleep

#Executavel do Aplicacao
executavel = "\\\\server\sistemas\oracle\oracle6i\\bin\ifrun60.exe"

#Arquivo a ser testado
caminhoForm = "D:\\DirForm\\Aplicacao4108.fmx"

#Dados de acesso ao AplicacaoD:\DirForm\Aplicacao4
login = "Usuario"
senha = "senha"
banco = "InstBanco"

#Executa o Aplicacao
shell = win32com.client.Dispatch("WScript.Shell")
programa = shell.Run(executavel)

#Fecha o Aplicacao na memoria
def fechaAplicacao():
    fechaAplicacao = "taskkill /IM ifrun60.exe /T /F"
    shell.Run(fechaAplicacao)

def ativaJanela(arquivo, nomeDaJanela):
    while (shell.AppActivate(nomeDaJanela) == False): print(str(arquivo) + ": Tentando acessar o aplicativo e focar a janela " + nomeDaJanela + "...");
    print("Janela: " + nomeDaJanela + " - Ativada")
    return True;

def ativaJanelaFinal(arquivo, nomeDaJanela):
    print(str(arquivo) + ": Tentando acessar o aplicativo e focar a janela " + nomeDaJanela + "...");
    if(shell.AppActivate(nomeDaJanela) == True):
        print(str(arquivo) + ": Janela " + nomeDaJanela + " focada com sucesso");
        #fechaAplicacao()
        return True;
    else:
        print(str(arquivo) + ": Nao foi possivel acessar a Janela " + nomeDaJanela);
        #fechaAplicacao()
        return False;

ativaJanela(caminhoForm, "Oracle Forms Runtime")

ativaJanela(caminhoForm, "Forms Runtime Options")
sleep(1)
shell.SendKeys(caminhoForm)
sleep(0.5)
shell.SendKeys("{TAB}")
shell.SendKeys(login)
sleep(0.5)
shell.SendKeys("{TAB}")
shell.SendKeys(senha)
sleep(0.5)
shell.SendKeys("{TAB}")
shell.SendKeys(banco)
sleep(0.5)
shell.SendKeys(18*"{TAB}")
shell.SendKeys("{ENTER}")

# Se o metodo retornar True o sistema impediu o acesso.
resultado = str(ativaJanelaFinal(caminhoForm, "Forms"))

#Coloca o resultado do teste em um arquivo de log
with open("resultado.txt", 'a') as resultadoArquivo:
    resultado = caminhoForm + ";" + str(resultado) + "\n"
    resultadoArquivo.write(resultado)
