######################################################################################
# Script em PowerShell para verificar os membros de um grupo local de varias maquinas#
######################################################################################

#Obtem a lista de maquinas (hostname)
$server = Get-Content "C:\TEMP\hdu.txt"

#Nome do grupo local a ser pesquisado
$localgroup = "Administradores"

foreach ($i in $server){
    
    Write-Host ''
    Write-Host '---'$i' ---'
    $group = ''
	$members = ''
	$group = [ADSI]"WinNT://$i/$localgroup,group"
    $members = $group.psbase.Invoke("Members")
    
    $members |
        ForEach-Object {
            $Nome = $_.GetType().InvokeMember("Name", 'GetProperty', $null, $_, $null)
            Write-Host 'Membro: ' $Nome 
        }

}
