#Obtem a listagem deusuarios locais
$computador = Get-Content "C:\TEMP\computador.txt"

foreach ($i in $computador){

    Write-Host ''
    Write-Host '---'$i' ---'

    $ADSI = [ADSI]"WinNT://$i"

    $Users = $ADSI.Children  | where {$_.SchemaClassName  -eq 'user'}

    $Users | Select Name,Description,LastLogin,flags

    #$Users | gm
 }
