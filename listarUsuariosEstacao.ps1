#$Computername = $env:COMPUTERNAME

$adsi = [ADSI]"WinNT://$Computername"

$Users = $adsi.Children  | where {$_.SchemaClassName -eq 'user'}

$Users 
