#Acessar os detalhes de atributos de usuarios do ActiveDirectory.

Import-Module ActiveDirectory

$attributes_aud = 'SamAccountName', 'Name', 'Mail', 'Title', 'Company', 'Department', 'WhenCreated', 'Enabled'

Get-ADUser -LDAPFilter "(sAMAccountName=usuario)" -Properties $attributes_aud | select $attributes_aud

#Se preferir, retorne todos os dados de uma vez. Descomente a linha abaixo.
#Get-ADUser -LDAPFilter "(sAMAccountName=usuario)" -Properties * | select *
