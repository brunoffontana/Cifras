import socket
import pyperclip
import func
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

key = 5
nova = func.CriptVegenere()
arquivoEncript = func.encript(nova,key)
print '***Mensagem criptografada*** \n'+arquivoEncript
tcp.send(arquivoEncript)
