###############################################################################################
# Script em PowerShell para verificar dados de usuarios e grupos oriundos do Active Directory #
###############################################################################################

#Obtem a lista de usuarios (sAMAccountName)
$usuarios = Get-Content "C:\TEMP\usuariosGS.txt"

#Importa o modulo do AD para o PowerShell
Import-Module ActiveDirectory

#Atributos a serem recuperados do AD
$attributes_aud = 'SamAccountName', 'distinguishedName', 'Name', 'Mail', 'Title', 'Company', 'Department', 'Description', 'extensionAttribute3', 'Office', 'WhenCreated', 'Enabled', 'UserAccountControl'

#Para cada usuario do arquivo texto, execute...
foreach ($i in $usuarios){
    
	Write-Host ''
    Write-Host '---'$i' ---'
    
    #Para retornar dados de um GRUPO
    #Get-ADGroup -LDAPFilter "(sAMAccountName=$i)" -Properties $attributes_aud | select $attributes_aud
    
    #Para retornar dados de um USUARIO
    Get-ADUser -LDAPFilter "(sAMAccountName=$i)" -Properties $attributes_aud | select $attributes_aud
}
