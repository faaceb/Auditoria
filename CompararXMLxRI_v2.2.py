# -*- coding: latin-1 -*-

#Arquivo contendo os dados dos XML
arquivoDadosXML = 'resultadoExtracaoXML_CBD_Jan16.csv'

#Arquivo contendo os dados do ERP RI
arquivoDadosRI = 'C:\\ProgramData\\MySQL\\MySQL Server 5.7\\Uploads\\ExtracaoRI_Jan16_a_Fev17.csv'
#arquivoDadosRI = 'Dezembro2016.csv'
#arquivoDadosRI = 'C:\\ProgramData\\MySQL\\MySQL Server 5.7\\Uploads\\ExtracaoRI_Jan16_a_Jun16.csv'
#arquivoDadosRI = 'C:\\ProgramData\\MySQL\\MySQL Server 5.7\\Uploads\\ExtracaoRI_Jul16_a_Dez16.csv'
#arquivoDadosRI = 'C:\\ProgramData\\MySQL\\MySQL Server 5.7\\Uploads\\ExtracaoRI_Jan17_a_Fev17.csv'

#Arquivo CSV resultante
#arquivoCSV = 'resultadoComparacao_CBD_Fev16.csv'
arquivoCSV = 'teste.csv'

#CARACTERES DE CONTROLE DE CSV
caractTerminador = '"'
caractSeparador = ';'

#CABECALHO DO ARQUIVO CSV
cabecalho = '%s%s%s%s' % (caractTerminador, "XML_CHAVE_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_CNPJ_EMISSOR", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_NR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_VALOR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_EMISSAO", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_NAT_OPER", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_CNPJ_DEST", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_ENCONTRADO_RI", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_CNPJ_EMISSOR", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_NR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_VALOR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_EMISSAO_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_DATA_GL", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_ORIGEM", caractTerminador, caractSeparador)

#Cria o Arquivo CSV e adiciona o cabecalho (campos)
with open(arquivoCSV, 'w+') as caminhoArquivoCSVAberto:
    caminhoArquivoCSVAberto.write(cabecalho)
    caminhoArquivoCSVAberto.write('\n') #Pular uma linha

#Inicializa a List onde serao armazenadas as linhas do ERP RI
cadaLinhaRi = []

print('%s%s' % ('LENDO BASE DO ERP RI - Arquivo: ', arquivoDadosRI))

#Abre o arquivo ERP RI
with open(arquivoDadosRI, 'r', encoding="latin1") as caminhoArquivoRIAberto:

    #Para cada linha, execute:
    for linha in caminhoArquivoRIAberto:

        #Cria uma List para cada elemento da linha
        #linha = linha.replace('"','')
        linha = linha.split(';')
    
        #Armazena os dados da linha nas variaveis
        riChaveNf = linha[38]
        riCnpjEmissor = linha[5]
        riNrNf = linha[16]
        riValorNf = linha[19].replace(',','').replace('.',',')
        riEmissao = linha[6]
        riDataGl = linha[10]
        riOrigem = linha[3]
        
        linhaRi = '%s%s' % (riChaveNf, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riCnpjEmissor, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riNrNf, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riValorNf, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riEmissao, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riDataGl, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riOrigem, caractSeparador)
        
        cadaLinhaRi.append(linhaRi)

#Contador de arquivos analisados
contador = 1

#Abre o arquivo XML
with open(arquivoDadosXML, 'r') as caminhoArquivoXMLAberto:

    xmlChaveNf = ''

    #Para cada linha, execute:
    for linha in caminhoArquivoXMLAberto:

        #Variavel que sera utilizada para ignorar a linha se a Chave da Nota ja tiver sido analisada
        xmlChaveNfUltimo = xmlChaveNf
        
        #Cria uma List para cada elemento da linha
        linha = linha.replace('"','')
        linha = linha.split(',')
        
        #Armazena os dados da linha nas variaveis
        xmlChaveNf = linha[0].replace('procNFE','').replace('.xml','')
        
        #ignorar a linha se a Chave da Nota ja tiver sido analisada
        if (xmlChaveNf == xmlChaveNfUltimo):
            continue

        xmlNrNf = linha[7]        
        xmCnpjEmissor = linha[22]
        xmlValorNf = linha[46]
        xmlEmissao = linha[8].split('T')[0]
        xmlNatOper = linha[3]
        xmlCnpjDest = linha[27]
        
        #Remove dados das variaveis do RI
        riChaveNf = ''
        riCnpjEmissor = ''
        riNrNf = ''
        riValorNf = ''
        riEmissao = ''
        riDataGl = ''
        riOrigem = ''
        
        #Verifica se os dados do XML existem na base do RI
        xmlEcontradoRi = 'N'
        for itensRi in cadaLinhaRi:
            ChaveNotaRi = itensRi.split(caractSeparador)[0]
            if (xmlChaveNf == ChaveNotaRi):
                xmlEcontradoRi = 'S'
                riCnpjEmissor = itensRi.split(caractSeparador)[1]
                riNrNf = itensRi.split(caractSeparador)[2]
                riValorNf = itensRi.split(caractSeparador)[3]
                riEmissao = itensRi.split(caractSeparador)[4]
                riDataGl = itensRi.split(caractSeparador)[5]
                riOrigem = itensRi.split(caractSeparador)[6]
        
        #Dados XML
        linhaTotal = '%s%s%s%s' % (caractTerminador, xmlChaveNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmCnpjEmissor, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlNrNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlValorNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlEmissao, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlNatOper, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlCnpjDest, caractTerminador, caractSeparador)

        #Diz se os dados da NF no XML foram encontradas na base do ERP RI
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlEcontradoRi, caractTerminador, caractSeparador)

        #Dados RI
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riCnpjEmissor, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riNrNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riValorNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riEmissao, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riDataGl, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riOrigem, caractTerminador, caractSeparador)
        
        with open(arquivoCSV, 'a+') as caminhoArquivoCSVAberto:
            caminhoArquivoCSVAberto.write('%s' % (linhaTotal))
            caminhoArquivoCSVAberto.write('\n') #Pular uma linha
        
        print('%s: %s' % (contador, linhaTotal))
        contador = contador + 1

print ('---PROCESSO FINALIZADO---')
