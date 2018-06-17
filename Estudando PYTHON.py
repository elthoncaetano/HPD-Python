Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 2+5
7
>>> print ("Elthon Caetano, OIII")
Elthon Caetano, OIII
>>> if (30>44) print("sim") else print("Não")
SyntaxError: invalid syntax
>>> if (30>44){ print("sim")} else {print("Não")}
SyntaxError: invalid syntax
>>> if (30>44)
SyntaxError: invalid syntax
>>> 44 == 22
False
>>> 44=2
SyntaxError: can't assign to literal
>>> elthon = "blz"
>>> print ("elthon")
elthon
>>> print (elthon)
blz
>>> type elthon
SyntaxError: invalid syntax
>>> type (elthon)
<class 'str'>
>>> mario = {"Mario","Luigi","princesa","Copa","Yoshi"}
>>> type (mario)
<class 'set'>
>>> print mario
SyntaxError: Missing parentheses in call to 'print'
>>> print (mario)
{'Yoshi', 'princesa', 'Luigi', 'Mario', 'Copa'}
>>> mario
{'Yoshi', 'princesa', 'Luigi', 'Mario', 'Copa'}
>>> mario.1
SyntaxError: invalid syntax
>>> elthon
'blz'
>>> 
>>> 
>>> cls
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> 
>>> clear
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> elthon[1]
'l'
>>> mario[1]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    mario[1]
TypeError: 'set' object does not support indexing
>>> mario[0]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    mario[0]
TypeError: 'set' object does not support indexing
>>> mario
{'Yoshi', 'princesa', 'Luigi', 'Mario', 'Copa'}
>>> mario = ["Mario","Luigi","princesa","Copa","Yoshi"]
>>> mario
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi']
>>> mario[1]
'Luigi'
>>> mario[1,2]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    mario[1,2]
TypeError: list indices must be integers or slices, not tuple
>>> mario[1;2]
SyntaxError: invalid syntax
>>> mario[1-2]
'Yoshi'
>>> mario[1][2]
'i'
>>> mario[1:2]]
SyntaxError: invalid syntax
>>> mario[1:2]
['Luigi']
>>> mario[1:3]
['Luigi', 'princesa']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> mario
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi']
>>> mario[1-*]
SyntaxError: invalid syntax
>>> mario[1:]
['Luigi', 'princesa', 'Copa', 'Yoshi']
>>> mario[:]
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi']
>>> mario
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi']
>>> sim
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    sim
NameError: name 'sim' is not defined
>>> elth['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi']
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    elth['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi']
NameError: name 'elth' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> elthon
'blz'
>>> 
>>> 
>>> 
>>> 
>>> mario = supermario
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    mario = supermario
NameError: name 'supermario' is not defined
>>> supermario = mario
>>> supermario
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi']
>>> supermario.append("wario")
>>> super
<class 'super'>
>>> supermario
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi', 'wario']
>>> "elthon" in supermario
False
>>> print(supermario.index("Copa"))
3
>>> print (supermario[3])
Copa
>>> supermario
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi', 'wario']
>>> supermario.insert
<built-in method insert of list object at 0x7ff0b3aaef88>
>>> supermario.insert(1,"peach")
>>> supermario
['Mario', 'peach', 'Luigi', 'princesa', 'Copa', 'Yoshi', 'wario']
>>> supermario.insert(0,"Tody")
>>> supermario
['Tody', 'Mario', 'peach', 'Luigi', 'princesa', 'Copa', 'Yoshi', 'wario']
>>> supermario.re
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    supermario.re
AttributeError: 'list' object has no attribute 're'
>>> supermario.remove("Tody")
>>> supermario
['Mario', 'peach', 'Luigi', 'princesa', 'Copa', 'Yoshi', 'wario']
>>> supermario.pop(1)
'peach'
>>> supermario
['Mario', 'Luigi', 'princesa', 'Copa', 'Yoshi', 'wario']
>>> supermario(')
	   
SyntaxError: EOL while scanning string literal
>>> supermario.pop(1)
'Luigi'
>>> supermario
['Mario', 'princesa', 'Copa', 'Yoshi', 'wario']
>>> supermario.pop(3)
'Yoshi'
>>> del(supermario[0])
>>> supermario
['princesa', 'Copa', 'wario']
>>> sort(supermario)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    sort(supermario)
NameError: name 'sort' is not defined
>>> supermario.sort()
>>> supermario
['Copa', 'princesa', 'wario']
>>> supermario = mario
>>> supermario.sor
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    supermario.sor
AttributeError: 'list' object has no attribute 'sor'
>>> supermario.sort()
>>> supermario
['Copa', 'princesa', 'wario']
>>> mario
['Copa', 'princesa', 'wario']
>>> supermario
['Copa', 'princesa', 'wario']
>>> sorted(supemario)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    sorted(supemario)
NameError: name 'supemario' is not defined
>>> sorted(supermario)
['Copa', 'princesa', 'wario']
>>> del(supermario[0])
>>> del(supermario[0])
>>> supermario
['wario']
>>> mario
['wario']
>>> supermario
['wario']
>>> mario = ["Mario","Luigi","princesa","Copa","Yoshi"]
>>> for nome in mario:
	print(nome)

	
Mario
Luigi
princesa
Copa
Yoshi
>>> >>> for nome in mario:
	print("O nome do personagem atual é %s" %nome)
	
SyntaxError: invalid syntax
>>> for nome in mario:
	print("O nome do personagem atual é %s" %nome)

	
O nome do personagem atual é Mario
O nome do personagem atual é Luigi
O nome do personagem atual é princesa
O nome do personagem atual é Copa
O nome do personagem atual é Yoshi
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> a=5
>>> b=8
>>> if a > b:
	print ("A variável A é maior que a B")
	else:
		
SyntaxError: invalid syntax
>>> if a > b:
	print ("A variável A é maior que a B")
else:
	print ("A variável B é maior que a A")

	
A variável B é maior que a A
>>> mario = ("Mario","Luigi","princesa","Copa","Yoshi")
>>> type.mario()
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    type.mario()
AttributeError: type object 'type' has no attribute 'mario'
>>> type(mario)
<class 'tuple'>
>>> cadastro={"nome":"Elthon", "Idade":"32", "Boniteza":"Nível Altíssimo","genero":"masculino"}
>>> cadastrp
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    cadastrp
NameError: name 'cadastrp' is not defined
>>> cadastro
{'Boniteza': 'Nível Altíssimo', 'nome': 'Elthon', 'Idade': '32', 'genero': 'masculino'}
>>> print (cadastro[nome])
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    print (cadastro[nome])
KeyError: 'Yoshi'
>>> print (cadastro["nome"])
Elthon
>>> print (cadastro.ke())
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    print (cadastro.ke())
AttributeError: 'dict' object has no attribute 'ke'
>>> print (cadastro.keys())
dict_keys(['Boniteza', 'nome', 'Idade', 'genero'])
>>> print (cadastro.values())
dict_values(['Nível Altíssimo', 'Elthon', '32', 'masculino'])
>>> for valor in cadastro.values():
	print (valor)

	
Nível Altíssimo
Elthon
32
masculino
>>> 
>>> 
>>> for chaves in cadastro.keys():
	print (chave)

	
Traceback (most recent call last):
  File "<pyshell#157>", line 2, in <module>
    print (chave)
NameError: name 'chave' is not defined
>>> for chaves in cadastro.keys():
	print (chave)

	
Traceback (most recent call last):
  File "<pyshell#160>", line 2, in <module>
    print (chave)
NameError: name 'chave' is not defined
>>> for chave  in cadastro.keys():
	print(chave)

	
Boniteza
nome
Idade
genero
>>> cadastro
{'Boniteza': 'Nível Altíssimo', 'nome': 'Elthon', 'Idade': '32', 'genero': 'masculino'}
>>> del(cadastro["boniteza"])
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    del(cadastro["boniteza"])
KeyError: 'boniteza'
>>> del(cadastro["Boniteza"])
>>> cadastro
{'nome': 'Elthon', 'Idade': '32', 'genero': 'masculino'}
>>> tarefas_do_dia = {"primeira":"responder emails","segunda":"tomar um café com o gerente do projeto","terceira":"criar receitas ou playbooks"}
>>> ta
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    ta
NameError: name 'ta' is not defined
>>> tarefas_do_dia
{'segunda': 'tomar um café com o gerente do projeto', 'terceira': 'criar receitas ou playbooks', 'primeira': 'responder emails'}
>>> tarefas_do_dia.popitem()
('segunda', 'tomar um café com o gerente do projeto')
>>> tarefas_do_dia.popitem()
('terceira', 'criar receitas ou playbooks')
>>> tarefas_do_dia.popitem()
('primeira', 'responder emails')
>>> tarefas_do_dia.popitem()
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    tarefas_do_dia.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> tarefas_do_dia = {"primeira":"responder emails","segunda":"tomar um café com o gerente do projeto","terceira":"criar receitas ou playbooks"}
>>> len(tarefas_do_dia )
3
>>> novas_tarefas={"quarta":"falar com o GP", "quinta":"ir embora"}
>>> novas_tarefas
{'quarta': 'falar com o GP', 'quinta': 'ir embora'}
>>> tarefas_do_dia.update(novas_tarefas)
>>> tarefas_do_dia
{'quarta': 'falar com o GP', 'quinta': 'ir embora', 'segunda': 'tomar um café com o gerente do projeto', 'terceira': 'criar receitas ou playbooks', 'primeira': 'responder emails'}
>>> sort(tarefas_do_dia)
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    sort(tarefas_do_dia)
NameError: name 'sort' is not defined
>>> tarefas_do_dia.sort()
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    tarefas_do_dia.sort()
AttributeError: 'dict' object has no attribute 'sort'
>>> sorted(tarefas_do_dia)
['primeira', 'quarta', 'quinta', 'segunda', 'terceira']
>>> tarefas_do_dia
{'quarta': 'falar com o GP', 'quinta': 'ir embora', 'segunda': 'tomar um café com o gerente do projeto', 'terceira': 'criar receitas ou playbooks', 'primeira': 'responder emails'}
>>> def imprimir_nomes():
	nomes = ["jeferson", "diego", "felipe", "gustavo"]
	for nome in nomes:
		print("O nome atual é: %s" % nome)

		
>>> 
>>> 
>>> imprimir_nomes
<function imprimir_nomes at 0x7ff0b3aaaea0>
>>> imprimir_nomes()
O nome atual é: jeferson
O nome atual é: diego
O nome atual é: felipe
O nome atual é: gustavo
>>> 
