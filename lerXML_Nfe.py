#############################################################################################
# Script para Leitura de arquivos XML com os dados de Notas Fiscais de Mercadoria do SEFAZ  #
#############################################################################################

from bs4 import BeautifulSoup
import os

#DIRETORIO ONDE ENCONTRAM-SE OS XML
diretorio = 'C:\\Users\\a37117\\Desktop\\XML_Fernanda'

#Arquivo CSV resultante
arquivoCSV = 'resultadoExtracaoXML_Fernanda.csv'

#CARACTERES DE CONTROLE DE CSV
caractTerminador = '"'
caractSeparador = ','

#CABECALHO DO ARQUIVO CSV
#INFORMACOES BASICAS
cabecalho = '%s%s%s%s' % (caractTerminador, "Arquivo_XML", caractTerminador, caractSeparador)
#cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "infNFe_ID", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_cUF', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_cNF', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_natOp', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_indPag', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_mod', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_serie', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_nNF', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_dhEmi', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_dhSaiEnt', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_tpNF', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_idDest', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_cMunFG', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_tpImp', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_tpEmis', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_cDV', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide__tpAmb', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_finNFe', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_indFinal', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_indPres', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_procEmi', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'ide_verProc', caractTerminador, caractSeparador)
#cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'NFref_refNFe', caractTerminador, caractSeparador)

#EMISSOR
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Emissor_CNPJ', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Emissor_xNome', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Emissor_xFant', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Emissor_IE', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Emissor_CRT', caractTerminador, caractSeparador)

#DESTINATARIO
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Dest_CNPJ', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Dest_xNome', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Dest_indIEDest', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Dest_IE', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Dest_email', caractTerminador, caractSeparador)
    
#Totais
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vBC', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vICMS', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vICMSDeson', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vBCST', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vST', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vProd', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vFrete', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vSeg', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vDesc', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vII', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vIPI', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vPIS', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vCOFINS', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vOutro', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vNF', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Totais_vTotTrib', caractTerminador, caractSeparador)
    
#TRANSPORTE
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Transp_modFrete', caractTerminador, caractSeparador)
    
#VOLUME
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Volume_qVol', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Volume_esp', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Volume_pesoL', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Volume_pesoB', caractTerminador, caractSeparador)

#INFORMACOES ADICIONAIS
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'InfAdic_infAdFisco', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'InfAdic_infCpl', caractTerminador, caractSeparador)

#Informacoes de Protocolo
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "infProt_Chave", caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, "infProt_xMotivo", caractTerminador, caractSeparador)

#ITENS
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_nItem', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_cProd', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_cEAN', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_xProd', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_NCM', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_CFOP', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_uCom', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_qCom', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_vUnCom', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_vProd', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_cEANTrib', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_uTrib', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_qTrib', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_vUnTrib', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Item_indTot', caractTerminador, caractSeparador)
    
#ITENS IMPOSTOS
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_vTotTrib', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_ICMS_orig', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_ICMS_CST', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_PIS_CST', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_PIS_vBC', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_PIS_pPIS', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_PIS_vPIS', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_COFINS_CST', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_COFINS_vBC', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_COFINS_pCOFINS', caractTerminador, caractSeparador)
cabecalho = '%s%s%s%s%s' % (cabecalho, caractTerminador, 'Itens_Imposto_COFINS_vCOFINS', caractTerminador, caractSeparador)

#Cria o Arquivo CSV e adiciona o cabecalho (campos)
with open(arquivoCSV, 'w+') as caminhoArquivoCSVAberto:
    caminhoArquivoCSVAberto.write(cabecalho)
    caminhoArquivoCSVAberto.write('\n') #Pular uma linha

#Contador
contador = 1

#Executa a extracao em cada arquivo XML contido no Diretorio
for arq in os.listdir(diretorio):
    arqCaminhoCompleto = '%s\%s' % (diretorio, arq)
    #print (arqCaminhoCompleto)

    #Abertura do Arquivo XML e Parse
    with open(arqCaminhoCompleto, 'r') as arquivoXML:
        f = arquivoXML.read()
        arqParsed = BeautifulSoup(f, "html.parser")

    #Coleta dos dados
    #if len(arqParsed.nfeproc.nfe.findAll('infnfe')) > 0: infNfe_attr_id = arqParsed.nfeproc.nfe.infnfe['id']
    #else: infNfe_attr_id = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('cuf')) > 0: infNfe_cUF = arqParsed.nfeproc.nfe.infnfe.findAll('cuf')[0].string 
    else: infNfe_cUF = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('cnf')) > 0: infNfe_cNF = arqParsed.nfeproc.nfe.infnfe.findAll('cnf')[0].string 
    else: infNfe_cNF = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('natop')) > 0: infNfe_natOp = arqParsed.nfeproc.nfe.infnfe.findAll('natop')[0].string 
    else: infNfe_natOp = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('indpag')) > 0: infNfe_indPag = arqParsed.nfeproc.nfe.infnfe.findAll('indpag')[0].string 
    else: infNfe_indPag = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('mod')) > 0: infNfe_mod = arqParsed.nfeproc.nfe.infnfe.findAll('mod')[0].string 
    else: infNfe_mod = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('serie')) > 0: infNfe_serie = arqParsed.nfeproc.nfe.infnfe.findAll('serie')[0].string 
    else: infNfe_serie = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('nnf')) > 0: infNfe_nNF = arqParsed.nfeproc.nfe.infnfe.findAll('nnf')[0].string 
    else: infNfe_nNF = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('dhemi')) > 0: infNfe_dhEmi = arqParsed.nfeproc.nfe.infnfe.findAll('dhemi')[0].string 
    else: infNfe_dhEmi = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('dhsaient')) > 0: infNfe_dhSaiEnt = arqParsed.nfeproc.nfe.infnfe.findAll('dhsaient')[0].string 
    else: infNfe_dhSaiEnt = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('tpnf')) > 0: infNfe_tpNF = arqParsed.nfeproc.nfe.infnfe.findAll('tpnf')[0].string 
    else: infNfe_tpNF = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('iddest')) > 0: infNfe_idDest = arqParsed.nfeproc.nfe.infnfe.findAll('iddest')[0].string 
    else: infNfe_idDest = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('cmunfg')) > 0: infNfe_cMunFG = arqParsed.nfeproc.nfe.infnfe.findAll('cmunfg')[0].string 
    else: infNfe_cMunFG = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('tpimp')) > 0: infNfe_tpImp = arqParsed.nfeproc.nfe.infnfe.findAll('tpimp')[0].string 
    else: infNfe_tpImp = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('tpemis')) > 0: infNfe_tpEmis = arqParsed.nfeproc.nfe.infnfe.findAll('tpemis')[0].string 
    else: infNfe_tpEmis = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('cdv')) > 0: infNfe_cDV = arqParsed.nfeproc.nfe.infnfe.findAll('cdv')[0].string 
    else: infNfe_cDV = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('tpamb')) > 0: infNfe_tpAmb = arqParsed.nfeproc.nfe.infnfe.findAll('tpamb')[0].string 
    else: infNfe_tpAmb = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('finnfe')) > 0: infNfe_finNFe = arqParsed.nfeproc.nfe.infnfe.findAll('finnfe')[0].string 
    else: infNfe_finNFe = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('indfinal')) > 0: infNfe_indFinal = arqParsed.nfeproc.nfe.infnfe.findAll('indfinal')[0].string 
    else: infNfe_indFinal = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('indpres')) > 0: infNfe_indPres = arqParsed.nfeproc.nfe.infnfe.findAll('indpres')[0].string 
    else: infNfe_indPres = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('procemi')) > 0: infNfe_procEmi = arqParsed.nfeproc.nfe.infnfe.findAll('procemi')[0].string 
    else: infNfe_procEmi = ''
    if len(arqParsed.nfeproc.nfe.infnfe.findAll('verproc')) > 0: infNfe_verProc = arqParsed.nfeproc.nfe.infnfe.findAll('verproc')[0].string 
    else: infNfe_verProc = ''
    if len(arqParsed.nfeproc.nfe.infnfe.emit.findAll('cnpj')) > 0: emi_CNPJ = arqParsed.nfeproc.nfe.infnfe.emit.findAll('cnpj')[0].string 
    else: emi_CNPJ = ''
    if len(arqParsed.nfeproc.nfe.infnfe.emit.findAll('xnome')) > 0: emi_xNome = arqParsed.nfeproc.nfe.infnfe.emit.findAll('xnome')[0].string 
    else: emi_xNome = ''
    if len(arqParsed.nfeproc.nfe.infnfe.emit.findAll('xfant')) > 0: emi_xFant = arqParsed.nfeproc.nfe.infnfe.emit.findAll('xfant')[0].string 
    else: emi_xFant = ''
    if len(arqParsed.nfeproc.nfe.infnfe.emit.findAll('ie')) > 0: emi_IE = arqParsed.nfeproc.nfe.infnfe.emit.findAll('ie')[0].string 
    else: emi_IE = ''
    if len(arqParsed.nfeproc.nfe.infnfe.emit.findAll('crt')) > 0: emi_CRT = arqParsed.nfeproc.nfe.infnfe.emit.findAll('crt')[0].string 
    else: emi_CRT = ''
    if len(arqParsed.nfeproc.nfe.infnfe.dest.findAll('cnpj')) > 0: dest_CNPJ = arqParsed.nfeproc.nfe.infnfe.dest.findAll('cnpj')[0].string 
    else: dest_CNPJ = ''
    if len(arqParsed.nfeproc.nfe.infnfe.dest.findAll('xnome')) > 0: dest_xNome = arqParsed.nfeproc.nfe.infnfe.dest.findAll('xnome')[0].string 
    else: dest_xNome = ''
    if len(arqParsed.nfeproc.nfe.infnfe.dest.findAll('indiedest')) > 0: dest_indIEDest = arqParsed.nfeproc.nfe.infnfe.dest.findAll('indiedest')[0].string 
    else: dest_indIEDest = ''
    if len(arqParsed.nfeproc.nfe.infnfe.dest.findAll('ie')) > 0: dest_IE = arqParsed.nfeproc.nfe.infnfe.dest.findAll('ie')[0].string 
    else: dest_IE = ''
    if len(arqParsed.nfeproc.nfe.infnfe.dest.findAll('email')) > 0: dest_email = arqParsed.nfeproc.nfe.infnfe.dest.findAll('email')[0].string 
    else: dest_email = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vbc')) > 0: Totais_vBC = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vbc')[0].string 
    else: Totais_vBC = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vicms')) > 0: Totais_vICMS = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vicms')[0].string 
    else: Totais_vICMS = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vicmsdeson')) > 0: Totais_vICMSDeson = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vicmsdeson')[0].string 
    else: Totais_vICMSDeson = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vbcst')) > 0: Totais_vBCST = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vbcst')[0].string 
    else: Totais_vBCST = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vst')) > 0: Totais_vST = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vst')[0].string 
    else: Totais_vST = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vprod')) > 0: Totais_vProd = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vprod')[0].string 
    else: Totais_vProd = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vfrete')) > 0: Totais_vFrete = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vfrete')[0].string 
    else: Totais_vFrete = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vseg')) > 0: Totais_vSeg = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vseg')[0].string 
    else: Totais_vSeg = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vdesc')) > 0: Totais_vDesc = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vdesc')[0].string 
    else: Totais_vDesc = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vii')) > 0: Totais_vII = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vii')[0].string 
    else: Totais_vII = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vipi')) > 0: Totais_vIPI = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vipi')[0].string 
    else: Totais_vIPI = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vpis')) > 0: Totais_vPIS = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vpis')[0].string 
    else: Totais_vPIS = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vcofins')) > 0: Totais_vCOFINS = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vcofins')[0].string 
    else: Totais_vCOFINS = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('voutro')) > 0: Totais_vOutro = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('voutro')[0].string 
    else: Totais_vOutro = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vnf')) > 0: Totais_vNF = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vnf')[0].string 
    else: Totais_vNF = ''
    if len(arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vtottrib')) > 0: Totais_vTotTrib = arqParsed.nfeproc.nfe.infnfe.total.icmstot.findAll('vtottrib')[0].string 
    else: Totais_vTotTrib = ''
    if len(arqParsed.nfeproc.nfe.infnfe.transp.findAll('modfrete')) > 0: Transp_modFrete = arqParsed.nfeproc.nfe.infnfe.transp.findAll('modfrete')[0].string 
    else: Transp_modFrete = ''
    
    #Se o elemento existir, execute
    if arqParsed.findAll('qvol'):
        if len(arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('qvol')) > 0: Volume_qVol = arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('qvol')[0].string 
        else: Volume_qVol = ''
    else: Volume_qVol = ''
    
    #Se o elemento existir, execute
    if arqParsed.findAll('esp'):
        if len(arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('esp')) > 0: Volume_esp = arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('esp')[0].string 
        else: Volume_esp = ''
    else: Volume_esp = ''
    
    #Se o elemento existir, execute
    if arqParsed.findAll('pesol'):
        if len(arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('pesol')) > 0: Volume_pesoL = arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('pesol')[0].string 
        else: Volume_pesoL = ''
    else: Volume_pesoL = ''
    
    #Se o elemento existir, execute
    if arqParsed.findAll('pesob'):
        if len(arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('pesob')) > 0: Volume_pesoB = arqParsed.nfeproc.nfe.infnfe.transp.vol.findAll('pesob')[0].string 
        else: Volume_pesoB = ''
    else: Volume_pesoB = ''
    
    #Se o elemento existir, execute
    if arqParsed.find('infadfisco'):
        if len(arqParsed.nfeproc.nfe.infnfe.infadic.findAll('infadfisco')) > 0: infAdic_infAdFisco = arqParsed.nfeproc.nfe.infnfe.infadic.findAll('infadfisco')[0].string 
        else: infAdic_infAdFisco = ''
    else: infAdic_infAdFisco = ''
    
    #Se o elemento existir, execute
    if arqParsed.find('infadfisco'):
        if len(arqParsed.nfeproc.nfe.infnfe.infadic.findAll('infcpl')) > 0: infAdic_infCpl = arqParsed.nfeproc.nfe.infnfe.infadic.findAll('infcpl')[0].string 
        else: infAdic_infCpl = ''
    else: infAdic_infCpl = ''
            
    if len(arqParsed.nfeproc.protnfe.infprot.findAll('chnfe')) > 0: infProt_chNfe = arqParsed.nfeproc.protnfe.infprot.findAll('chnfe')[0].string 
    else: infProt_chNfe = ''
    if len(arqParsed.nfeproc.protnfe.infprot.findAll('xmotivo')) > 0: infProt_xMotivo = arqParsed.nfeproc.protnfe.infprot.findAll('xmotivo')[0].string 
    else: infProt_xMotivo = ''

    #Comeco da linha do registro do CSV
    linha = '%s%s%s%s' % (caractTerminador, arq, caractTerminador, caractSeparador)
    
    #Construcao da linha a partir da coleta dos dados do XML
    #linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_attr_id, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_cUF, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_cNF, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_natOp, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_indPag, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_mod, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_serie, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_nNF, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_dhEmi, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_dhSaiEnt, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_tpNF, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_idDest, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_cMunFG, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_tpImp, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_tpEmis, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_cDV, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_tpAmb, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_finNFe, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_indFinal, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_indPres, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_procEmi, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infNfe_verProc, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, emi_CNPJ, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, emi_xNome, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, emi_xFant, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, emi_IE, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, emi_CRT, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, dest_CNPJ, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, dest_xNome, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, dest_indIEDest, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, dest_IE, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, dest_email, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vBC, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vICMS, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vICMSDeson, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vBCST, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vST, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vProd, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vFrete, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vSeg, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vDesc, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vII, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vIPI, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vPIS, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vCOFINS, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vOutro, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vNF, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Totais_vTotTrib, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Transp_modFrete, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Volume_qVol, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Volume_esp, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Volume_pesoL, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, Volume_pesoB, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infAdic_infAdFisco, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infAdic_infCpl, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infProt_chNfe, caractTerminador, caractSeparador)
    linha = '%s%s%s%s%s' % (linha, caractTerminador, infProt_xMotivo, caractTerminador, caractSeparador)

    #Dados dos Itens
    ItensDados = []
    ItensDados = arqParsed.nfeproc.nfe.infnfe.findAll('det')

    #Quantidade de itens da NF
    qtdItens = len(ItensDados)

    #Para cada item da NF, execute:
    for Itens in range(0, qtdItens):
        
        #Inicializacao de variaveis
        linhaItem = ""
        Itens_Imposto_PIS_CST = ""
        Itens_Imposto_PIS_vBC = ""
        Itens_Imposto_PIS_pPIS = ""
        Itens_Imposto_PIS_vPIS = ""
        Itens_Imposto_COFINS_CST = ""
        Itens_Imposto_COFINS_vBC = ""
        Itens_Imposto_COFINS_pCOFINS = ""
        Itens_Imposto_COFINS_vCOFINS = ""
        
        #Parse dos dados dos itens
        arqParsed_Itens = BeautifulSoup(str(ItensDados[Itens]), "html.parser")
        atributosDet = arqParsed_Itens.find('det').attrs
        
        #Coleta dos dados de cada item da NF
        if qtdItens > 0: Item_nItem = atributosDet['nitem']
        else: Item_nItem = ''
        if len(arqParsed_Itens.det.prod.findAll('cprod')) > 0: Item_cProd = arqParsed_Itens.det.prod.findAll('cprod')[0].string 
        else: Item_cProd = ''
        if len(arqParsed_Itens.det.prod.findAll('cean')) > 0: Item_cEAN = arqParsed_Itens.det.prod.findAll('cean')[0].string 
        else: Item_cEAN = ''
        if len(arqParsed_Itens.det.prod.findAll('xprod')) > 0: Item_xProd = arqParsed_Itens.det.prod.findAll('xprod')[0].string 
        else: Item_xProd = ''
        if len(arqParsed_Itens.det.prod.findAll('ncm')) > 0: Item_NCM = arqParsed_Itens.det.prod.findAll('ncm')[0].string 
        else: Item_NCM = ''
        if len(arqParsed_Itens.det.prod.findAll('cfop')) > 0: Item_CFOP = arqParsed_Itens.det.prod.findAll('cfop')[0].string 
        else: Item_CFOP = ''
        if len(arqParsed_Itens.det.prod.findAll('ucom')) > 0: Item_uCom = arqParsed_Itens.det.prod.findAll('ucom')[0].string 
        else: Item_uCom = ''
        if len(arqParsed_Itens.det.prod.findAll('qcom')) > 0: Item_qCom = arqParsed_Itens.det.prod.findAll('qcom')[0].string 
        else: Item_qCom = ''
        if len(arqParsed_Itens.det.prod.findAll('vuncom')) > 0: Item_vUnCom = arqParsed_Itens.det.prod.findAll('vuncom')[0].string 
        else: Item_vUnCom = ''
        if len(arqParsed_Itens.det.prod.findAll('vprod')) > 0: Item_vProd = arqParsed_Itens.det.prod.findAll('vprod')[0].string 
        else: Item_vProd = ''
        if len(arqParsed_Itens.det.prod.findAll('ceantrib')) > 0: Item_cEANTrib = arqParsed_Itens.det.prod.findAll('ceantrib')[0].string 
        else: Item_cEANTrib = ''
        if len(arqParsed_Itens.det.prod.findAll('utrib')) > 0: Item_uTrib = arqParsed_Itens.det.prod.findAll('utrib')[0].string 
        else: Item_uTrib = ''
        if len(arqParsed_Itens.det.prod.findAll('qtrib')) > 0: Item_qTrib = arqParsed_Itens.det.prod.findAll('qtrib')[0].string 
        else: Item_qTrib = ''
        if len(arqParsed_Itens.det.prod.findAll('vuntrib')) > 0: Item_vUnTrib = arqParsed_Itens.det.prod.findAll('vuntrib')[0].string 
        else: Item_vUnTrib = ''
        if len(arqParsed_Itens.det.prod.findAll('indtot')) > 0: Item_indTot = arqParsed_Itens.det.prod.findAll('indtot')[0].string 
        else: Item_indTot = ''
    
        #Impostos - ICMS
        if len(arqParsed_Itens.det.imposto.findAll('vtottrib')) > 0: Itens_Imposto_vTotTrib = arqParsed_Itens.det.imposto.findAll('vtottrib')[0].string 
        else: Itens_Imposto_vTotTrib = ''
        if len(arqParsed_Itens.det.imposto.findAll('vtottrib')) > 0: Itens_Imposto_vTotTrib = arqParsed_Itens.det.imposto.findAll('vtottrib')[0].string 
        else: Itens_Imposto_vTotTrib = ''
        
        #Impostos - ICMS
        if arqParsed_Itens.find('icms40'):
            if len(arqParsed_Itens.det.imposto.icms.icms40.findAll('orig')) > 0: Itens_Imposto_ICMS_orig = arqParsed_Itens.det.imposto.icms.icms40.findAll('orig')[0].string 
            else: Itens_Imposto_ICMS_orig = ''
            if len(arqParsed_Itens.det.imposto.icms.icms40.findAll('cst')) > 0: Itens_Imposto_ICMS_CST = arqParsed_Itens.det.imposto.icms.icms40.findAll('cst')[0].string 
            else: Itens_Imposto_ICMS_CST = ''
        
        #Impostos - ICMS
        if arqParsed_Itens.find('icms00'):
            if len(arqParsed_Itens.det.imposto.icms.icms00.findAll('orig')) > 0: Itens_Imposto_ICMS_orig = arqParsed_Itens.det.imposto.icms.icms00.findAll('orig')[0].string 
            else: Itens_Imposto_ICMS_orig = ''
            if len(arqParsed_Itens.det.imposto.icms.icms00.findAll('cst')) > 0: Itens_Imposto_ICMS_CST = arqParsed_Itens.det.imposto.icms.icms00.findAll('cst')[0].string 
            else: Itens_Imposto_ICMS_CST = ''

        #Impostos - ICMS
        if arqParsed_Itens.find('icmssn102'):
            if len(arqParsed_Itens.det.imposto.icms.icmssn102.findAll('orig')) > 0: Itens_Imposto_ICMS_orig = arqParsed_Itens.det.imposto.icms.icmssn102.findAll('orig')[0].string 
            else: Itens_Imposto_ICMS_orig = ''
            if len(arqParsed_Itens.det.imposto.icms.icmssn102.findAll('cst')) > 0: Itens_Imposto_ICMS_CST = arqParsed_Itens.det.imposto.icms.icmssn102.findAll('cst')[0].string
            else: Itens_Imposto_ICMS_CST = ''
        
        #Impostos - PIS
        if arqParsed_Itens.find('pisoutr'):
            if len(arqParsed_Itens.det.imposto.pis.pisoutr.findAll('cst')) > 0: Itens_Imposto_PIS_CST = arqParsed_Itens.det.imposto.pis.pisoutr.findAll('cst')[0].string 
            else: Itens_Imposto_PIS_CST = ''
            if len(arqParsed_Itens.det.imposto.pis.pisoutr.findAll('vbc')) > 0: Itens_Imposto_PIS_vBC = arqParsed_Itens.det.imposto.pis.pisoutr.findAll('vbc')[0].string 
            else: Itens_Imposto_PIS_vBC = ''
            if len(arqParsed_Itens.det.imposto.pis.pisoutr.findAll('ppis')) > 0: Itens_Imposto_PIS_pPIS = arqParsed_Itens.det.imposto.pis.pisoutr.findAll('ppis')[0].string 
            else: Itens_Imposto_PIS_pPIS = ''
            if len(arqParsed_Itens.det.imposto.pis.pisoutr.findAll('vpis')) > 0: Itens_Imposto_PIS_vPIS = arqParsed_Itens.det.imposto.pis.pisoutr.findAll('vpis')[0].string 
            else: Itens_Imposto_PIS_vPIS = ''
        
        if arqParsed_Itens.find('pisaliq'):
            if len(arqParsed_Itens.det.imposto.pis.pisaliq.findAll('cst')) > 0: Itens_Imposto_PIS_CST = arqParsed_Itens.det.imposto.pis.pisaliq.findAll('cst')[0].string 
            else: Itens_Imposto_PIS_CST = ''
            if len(arqParsed_Itens.det.imposto.pis.pisaliq.findAll('vbc')) > 0: Itens_Imposto_PIS_vBC = arqParsed_Itens.det.imposto.pis.pisaliq.findAll('vbc')[0].string 
            else: Itens_Imposto_PIS_vBC = ''
            if len(arqParsed_Itens.det.imposto.pis.pisaliq.findAll('ppis')) > 0: Itens_Imposto_PIS_pPIS = arqParsed_Itens.det.imposto.pis.pisaliq.findAll('ppis')[0].string 
            else: Itens_Imposto_PIS_pPIS = ''
            if len(arqParsed_Itens.det.imposto.pis.pisaliq.findAll('vpis')) > 0: Itens_Imposto_PIS_vPIS = arqParsed_Itens.det.imposto.pis.pisaliq.findAll('vpis')[0].string 
            else: Itens_Imposto_PIS_vPIS = ''

        if arqParsed_Itens.find('pisnt'):
            if len(arqParsed_Itens.det.imposto.pis.pisnt.findAll('cst')) > 0: Itens_Imposto_PIS_CST = arqParsed_Itens.det.imposto.pis.pisnt.findAll('cst')[0].string 
            else: Itens_Imposto_PIS_CST = ''
            if len(arqParsed_Itens.det.imposto.pis.pisnt.findAll('vbc')) > 0: Itens_Imposto_PIS_vBC = arqParsed_Itens.det.imposto.pis.pisnt.findAll('vbc')[0].string 
            else: Itens_Imposto_PIS_vBC = ''
            if len(arqParsed_Itens.det.imposto.pis.pisnt.findAll('ppis')) > 0: Itens_Imposto_PIS_pPIS = arqParsed_Itens.det.imposto.pis.pisnt.findAll('ppis')[0].string 
            else: Itens_Imposto_PIS_pPIS = ''
            if len(arqParsed_Itens.det.imposto.pis.pisnt.findAll('vpis')) > 0: Itens_Imposto_PIS_vPIS = arqParsed_Itens.det.imposto.pis.pisnt.findAll('vpis')[0].string 
            else: Itens_Imposto_PIS_vPIS = ''
        
        #Impostos - COFINS
        if arqParsed_Itens.find('cofinsoutr'):
            if len(arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('cst')) > 0: Itens_Imposto_COFINS_CST = arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('cst')[0].string 
            else: Itens_Imposto_COFINS_CST = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('vbc')) > 0: Itens_Imposto_COFINS_vBC = arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('vbc')[0].string 
            else: Itens_Imposto_COFINS_vBC = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('pcofins')) > 0: Itens_Imposto_COFINS_pCOFINS = arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('pcofins')[0].string 
            else: Itens_Imposto_COFINS_pCOFINS = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('vcofins')) > 0: Itens_Imposto_COFINS_vCOFINS = arqParsed_Itens.det.imposto.cofins.cofinsoutr.findAll('vcofins')[0].string 
            else: Itens_Imposto_COFINS_vCOFINS = ''

        #Impostos - COFINS
        if arqParsed_Itens.find('cofinsaliq'):
            if len(arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('cst')) > 0: Itens_Imposto_COFINS_CST = arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('cst')[0].string 
            else: Itens_Imposto_COFINS_CST = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('vbc')) > 0: Itens_Imposto_COFINS_vBC = arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('vbc')[0].string 
            else: Itens_Imposto_COFINS_vBC = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('pcofins')) > 0: Itens_Imposto_COFINS_pCOFINS = arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('pcofins')[0].string 
            else: Itens_Imposto_COFINS_pCOFINS = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('vcofins')) > 0: Itens_Imposto_COFINS_vCOFINS = arqParsed_Itens.det.imposto.cofins.cofinsaliq.findAll('vcofins')[0].string 
            else: Itens_Imposto_COFINS_vCOFINS = ''

        #Impostos - COFINS
        if arqParsed_Itens.find('cofinsnt'):
            if len(arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('cst')) > 0: Itens_Imposto_COFINS_CST = arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('cst')[0].string 
            else: Itens_Imposto_COFINS_CST = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('vbc')) > 0: Itens_Imposto_COFINS_vBC = arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('vbc')[0].string 
            else: Itens_Imposto_COFINS_vBC = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('pcofins')) > 0: Itens_Imposto_COFINS_pCOFINS = arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('pcofins')[0].string 
            else: Itens_Imposto_COFINS_pCOFINS = ''
            if len(arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('vcofins')) > 0: Itens_Imposto_COFINS_vCOFINS = arqParsed_Itens.det.imposto.cofins.cofinsnt.findAll('vcofins')[0].string 
            else: Itens_Imposto_COFINS_vCOFINS = ''
    
        #Acrescenta os dados dos produtos a linha do CSV
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_nItem, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_cProd, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_cEAN, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_xProd, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_NCM, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_CFOP, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_uCom, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_qCom, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_vUnCom, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_vProd, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_cEANTrib, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_uTrib, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_qTrib, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_vUnTrib, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Item_indTot, caractTerminador, caractSeparador)

        #Impostos
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_vTotTrib, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_ICMS_orig, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_ICMS_CST, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_PIS_CST, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_PIS_vBC, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_PIS_pPIS, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_PIS_vPIS, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_COFINS_CST, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_COFINS_vBC, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_COFINS_pCOFINS, caractTerminador, caractSeparador)
        linhaItem = '%s%s%s%s%s' % (linhaItem, caractTerminador, Itens_Imposto_COFINS_vCOFINS, caractTerminador, caractSeparador)

        #Adiciona a linha de registro ao arquivo CSV
        with open(arquivoCSV, 'a+') as caminhoArquivoCSVAberto:
            caminhoArquivoCSVAberto.write('%s%s' % (linha, linhaItem))
            caminhoArquivoCSVAberto.write('\n') #Pular uma linha
        
        #print('%s%s%s' % ('Arquivo: ', arq, ' - Processo.'))

    print('%s: %s%s%s' % (contador, 'Arquivo: ', arq, ' - Processado.'))
    contador = contador + 1

print ('---PROCESSO FINALIZADO---')
