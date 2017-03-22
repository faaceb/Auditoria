#Arquivo contendo os dados dos XML
arquivoDadosXML = 'resultadoExtracaoXML_VENANCIO.csv'

#Arquivo contendo os dados do ERP RI
arquivoDadosRI = 'Dezembro2016.csv'

#Arquivo CSV resultante
arquivoCSV = 'resultadoComparacao.csv'

#CARACTERES DE CONTROLE DE CSV
caractTerminador = '"'
caractSeparador = ','

#CABECALHO DO ARQUIVO CSV
cabecalho = '%s%s%s%s' % (caractTerminador, "XML_CHAVE_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_NR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_VALOR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_EMISSAO", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "XML_ENCONTRADO_RI", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_NR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_VALOR_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_EMISSAO_NF", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "RI_DATA_GL", caractTerminador, caractSeparador)

#Cria o Arquivo CSV e adiciona o cabecalho (campos)
with open(arquivoCSV, 'w+') as caminhoArquivoCSVAberto:
    caminhoArquivoCSVAberto.write(cabecalho)
    caminhoArquivoCSVAberto.write('\n') #Pular uma linha

#Inicializa a List onde serao armazenadas as linhas do ERP RI
cadaLinhaRi = []

print('%s%s' % ('LENDO BASE DO ERP RI - Arquivo: ', arquivoDadosRI))

#Abre o arquivo ERP RI
with open(arquivoDadosRI, 'r') as caminhoArquivoRIAberto:

    #Para cada linha, execute:
    for linha in caminhoArquivoRIAberto:

        #Cria uma List para cada elemento da linha
        #linha = linha.replace('"','')
        linha = linha.split(';')
    
        #Armazena os dados da linha nas variaveis
        riChaveNf = linha[38]
        riNrNf = linha[16]
        riValorNf = linha[19]
        riEmissao = linha[6]
        riDataGl = linha[10]
        
        linhaRi = '%s%s' % (riChaveNf, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riNrNf, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riEmissao, caractSeparador)
        linhaRi = '%s%s%s' % (linhaRi, riDataGl, caractSeparador)
        
        cadaLinhaRi.append(linhaRi)

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
        xmlValorNf = linha[46]
        xmlEmissao = linha[8].split('T')[0]
        
        #Verifica se os dados do XML existem na base do RI
        xmlEcontradoRi = 'N'
        for itensRi in cadaLinhaRi:
            ChaveNotaRi = itensRi.split(',')[0]
            if (xmlChaveNf == ChaveNotaRi):
                xmlEcontradoRi = 'S'
        
        #Dados XML
        linhaTotal = '%s%s%s%s' % (caractTerminador, xmlChaveNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlNrNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlValorNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlEmissao, caractTerminador, caractSeparador)

        #Diz se os dados da NF no XML foram encontradas na base do ERP RI
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, xmlEcontradoRi, caractTerminador, caractSeparador)

        #Dados RI
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riNrNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riValorNf, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riEmissao, caractTerminador, caractSeparador)
        linhaTotal = '%s%s%s%s%s' % (linhaTotal, caractTerminador, riDataGl, caractTerminador, caractSeparador)
        
        print('%s' % (linhaTotal))