import socket
import pyperclip
import func
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

message = raw_input()

while message != 'x':
	key=3
	func.encript(message,key)	      
	msg = func.encript(message,key)
	tcp.send (msg)
	message = raw_input()
