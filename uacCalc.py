# -*- coding: iso-8859-1 -*-

dictUAC = {
	"ACCOUNTDISABLE ": 2,
	"DONT_EXPIRE_PASSWORD": 65536,
	"DONT_REQ_PREAUTH": 4194304,
	"ENCRYPTED_TEXT_PWD_ALLOWED": 128,
	"HOMEDIR_REQUIRED": 8,
	"LOCKOUT": 16,
	"NORMAL_ACCOUNT": 512,
	"PASSWD_CANT_CHANGE": 64,
	"PASSWD_NOTREQD": 32,
	"PASSWORD_EXPIRED": 8388608,
	"SCRIPT": 1,
	"SMARTCARD_REQUIRED": 262144,
	"TEMP_DUPLICATE_ACCOUNT": 256,
	"INTERDOMAIN_TRUST_ACCOUNT": 2048,
	"WORKSTATION_TRUST_ACCOUNT": 4096,
	"SERVER_TRUST_ACCOUNT": 8192,
	"MNS_LOGON_ACCOUNT": 131072,
	"TRUSTED_FOR_DELEGATION": 524288,
	"NOT_DELEGATED": 1048576,
	"USE_DES_KEY_ONLY": 2097152,
	"TRUSTED_TO_AUTH_FOR_DELEGATION": 16777216,
	"PARTIAL_SECRETS_ACCOUNT": 67108864
}

def uacCalc(uac, dictUAC):
	ultElem = [0]
	for value in sorted (dictUAC.values()):
		if (uac - value) < 0:
			uac -= ultElem[-1]
			break
		ultElem.append(value)
	return uac

code = [512,
	514,
	66048,
	2080,
	66080,
	66050,
	66082,
	546,
	544,
	4194946,
	4260354,
	4260352]

for item in code:
	itemAtual = item
	status = False
	while status != True:
		item = uacCalc(item, dictUAC)
		if item == 2:
			res = "INATIVO"
			status = True
		elif item == 0:
			res = "ATIVO"
			status = True
	print('%s:%s' % (itemAtual,res))
