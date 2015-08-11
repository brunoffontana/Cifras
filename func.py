def encript(message,key): 
	
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translated = ''
	message = message.upper()
	
	for symbol in message:
		 if symbol in LETTERS:
			 num = LETTERS.find(symbol) 
			 num = num + key
			 if num >= len(LETTERS):
				 num = num - len(LETTERS)
			 elif num < 0:
				 num = num + len(LETTERS)

			
			 translated = translated + LETTERS[num]

		 else:
			translated = translated + symbol
	return translated

def decrypt(message,key):

	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translated = ''
	message = message.upper()
	
	for symbol in message:
		 if symbol in LETTERS:
			 num = LETTERS.find(symbol) 
			 num = num - key
			 if num >= len(LETTERS):
				 num = num - len(LETTERS)
			 elif num < 0:
				 num = num + len(LETTERS)
			
			 translated = translated + LETTERS[num]

		 else:
			translated = translated + symbol
	return translated

def leArquivo():
	letter = 'abcdefghijklmnopqrstuvwxyz123456789'
	f = open("files.txt","r")
	for linha in f:
		nova = linha.rstrip()
		print len(linha)
		for i in range(0,len(linha)):
			if linha[i] in letter:
				nova = nova + linha[i]
		print nova
		return nova
	f.close()

def leArquivo2():
	f = open("files.txt","r")
	msg = f.readlines()
	#msg = msg.replace(' ','#')
	for i in range(len(msg)):
		msg_c = msg[i].replace(' ','#')
		print msg_c
	print '***Mensagem original*** \n'+msg_c
	return msg_c
	f.close()
	
def leArquivo3():
	f = open("files.txt","r")
	for line in f.readlines():
		line = line.replace(' ','#')
		print line
	return line
	f.close()
	
def decryptSub1(texto, key):
        texto_plano = ''
        texto = texto.replace(' ', '-')
        for i in range(key):
            for j in range(0, len(texto), key):
                texto_plano += texto[i + j]
        texto_plano=texto_plano.replace('-', ' ')
        texto_plano=texto_plano.replace('$', '')                
        return texto_plano.upper()

def CriptVegenere():
	f = open("files.txt","r")
	for line in f.readlines():
		line = line.replace(' ','#')
		print line
	return line
	f.close()
