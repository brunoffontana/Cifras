#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
abc = 'abcdefghijklmnopqrstuvwxyz'
 
def cifrar(cadeia, chave):
	text_cifrar = ''
 
	i = 0
	for letra in cadeia:
		suma = abc.find(letra) + abc.find(chave[i % len(chave)])
		modulo = int(suma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1
 
	return text_cifrar
 
def descifrar(cadeia, chave):
	text_cifrar = ''
 
	i = 0
	for letra in cadeia:
		soma = abc.find(letra) - abc.find(chave[i % len(chave)])
		modulo = int(soma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1
 
	return text_cifrar
 
 
def main():
	c = open("files.txt","r")
	msg = c.readlines()
	for i in range(len(msg)):
		msg_c = msg[i]
	chave = str(raw_input('chave: ')).lower()
	print cifrar(msg_c,chave)
	
	
	d = open("files.txt","r")
	msg = d.readlines()
	for i in range(len(msg)):
		msg_d = msg[i]
	chave = str(raw_input('chave: ')).lower()
	print descifrar(msg_d,chave)
 
 
if __name__ == '__main__':
	main()
