#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
abc = 'abcdefghijklmnopqrstuvwxyz '
 
 
def descifrar(cadeia, chave):
	text_cifrar = ''
 
	i = 0
	for letra in cadeia:
		soma = abc.find(letra) - abc.find(chave[i % len(chave)])
		modulo = int(soma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1
 
	return text_cifrar

def cifrar(cadeia, chave):
	text_cifrar = ''
 
	i = 0
	for letra in cadeia:
		soma = abc.find(letra) + abc.find(chave[i % len(chave)])
		modulo = int(soma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1
 
	return text_cifrar 
 
def main():
	c = str(raw_input()).lower()
	chave = str(raw_input('Digite a chave: ')).lower()
	print cifrar(c,chave)
	c = str(raw_input()).lower()
	chave = str(raw_input('Digite a chave: ')).lower()
	print descifrar(c,chave)
 
 
if __name__ == '__main__':
	main()
