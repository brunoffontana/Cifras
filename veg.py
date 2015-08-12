import func

key = 'aaa'
nova = func.CriptVegenere()
arquivoEncript = func.encript(nova,key)
print 'Mensagem criptografada \n'+arquivoEncript

arquivoDecript = func.decript(arquivoEncript,key)

print 'Mensagem Descriptografada \n'+arquivoDecript



