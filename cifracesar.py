import func

key = 3
nova = func.leArquivo()
arquivoEncript = func.encript(nova,key)
print 'Mensagem criptografada \n'+arquivoEncript

arquivoDecript = func.decript(arquivoEncript,key)

print 'Mensagem Descriptografada \n'+arquivoDecript



