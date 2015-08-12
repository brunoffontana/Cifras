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

def decript(message,key):

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
		for i in range(0,len(linha)):
			if linha[i] in letter:
				nova = nova + linha[i]
		print nova
		return nova
	f.close()



def CriptVegenere():
	f = open("files.txt","r")
	for line in f.readlines():
		line = line.replace(' ','#')
		print line
	return line
	f.close()
