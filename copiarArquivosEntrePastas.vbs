'Cria um objeto de sistema do tipo arquivo
Set fso=CreateObject("Scripting.FileSystemObject")

'Ajusta as variáveis com os endereços de origem e destino
Dim origem, destino
origem = "C:\Users\fabioaac\Documents\Pasta1\"
destino = "C:\Users\fabioaac\Documents\Pasta2\"

'Ajusta na variável fldr um objeto que representa a pasta de origem
Set fldr=fso.getFolder(origem)

'Contador de arquivos movidos
contador = 0

'Para cada arquivo na pasta, mova o arquivo, da origem para o destino
for Each file in fldr.Files
	file.Move(destino)
	contador = contador + 1
Next

MsgBox contador & " arquivo(s) movido(s) com sucesso."
