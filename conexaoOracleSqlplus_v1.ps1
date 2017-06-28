#########################################################################
# Diretoria de Auditoria Corporativa                                    #
# Script em PowerShell para conexao com banco de dados Oracle (sqlplus) #
#########################################################################

#Obtem a lista de servidor_usuario_senha_instancia
#Exemplo: SERVIDOR;USUARIO;SENHA;INSTANCIA (um por linha)
$registro = Get-Content "C:\TEMP\servidor_usuario_senha_instancia.txt"

#Separador utilizado para distinguir entre hostname, usuario e instancia
$separador = ';'

foreach ($i in $registro){

    $hostname = $i.split($separador)[0]
    $usuario = $i.split($separador)[1]
    $senha = $i.split($separador)[2]
    $instancia = $i.split($separador)[3]
    
	Write-Host ''
    Write-Host '---'$i' ---'
    Write-Host ''
    echo "SELECT SYS_CONTEXT ('USERENV', 'SESSION_USER') FROM DUAL;" | C:\instantclient_12_2\sqlplus $usuario/$senha@$hostname/$instancia
    
    Write-Host ''
    
}
