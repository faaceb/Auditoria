###########################################################################
# Script em PowerShell para efetuar ping em diversas estacoes de trabalho #
###########################################################################

#Obtem a lista de maquinas (hostname)
$server = Get-Content "C:\TEMP\estacoesEstoquePing.txt"

#Para cada maquina (linha do arquivo) execute...
foreach ($i in $server){
    
    Write-Host ''
    Write-Host '---'$i' ---'
    
    #Comando ping com 3 execucoes (-n 3)
    ping -n 3 $i

}

Write-Host ''
Write-Host '--- FIM DO SCRIPT ---'
