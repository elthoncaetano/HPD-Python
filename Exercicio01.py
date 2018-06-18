#!/usr/bin/env python3

#1 - Criar uma função que crie um diretório e dentro dele arquivos,
# utilizando o range para nomea-los, de 1 a 39;

import subprocess

def NewDir():
	global opa #definida como global para ser utilizada em outra função
	opa = input("Digite o nome do dir desejado: ")
	subprocess.call(['mkdir', opa])
	for newArq in range (1,40):
		subprocess.call(['touch', str(newArq)], cwd=opa)

#2 - Criar uma função para listar esses arquivos;

def list_dir():
	subprocess.call(['ls',opa])

########################

NewDir()
list_dir()
