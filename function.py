#!/usr/bin/env python3

def pause():
	input("\n\nPrecione enter para continuar...\n\n")

def mensagemFim():
	print ("Valeu por usar esse programa!")
	print ("VAIIII")

def imprimaTresLinhas():
	for i in range(1,4):
		print ('Esta é a linha' + str(i))

def imprimaNoveLinhas():
	for i in range(1,4):
		imprimaTresLinhas()

def mensagemInicio():
	print("Este programa é somente para mostrar como funciona o uso do functions")
	pause()

def linhaBranco():
	print()

def limpaTela():
	for i in range(1,26):
		linhaBranco()

#mensagemInicio()
limpaTela()
#print ("Testando a abagaça!")
#imprimaTresLinhas()
#pause()
#limpaTela()
#imprimaNoveLinhas()
#linhaBranco()
#imprimaNoveLinhas()
