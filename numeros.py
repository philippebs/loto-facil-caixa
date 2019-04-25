#!/usr/bin/python
import loto

todos_numeros = []

def popula_numeros():
	print('Populando numeros')
	global todos_numeros 
	todos_numeros = loto.createListNumber()
	rastreio_numeros([1, 10, 13])
	#print(todos_numeros)

def rastreio_numeros(lista_numeros_escolhidos):
	#print(todos_numeros)
	lista_numeros_escolhidos.sort()
	for numeros_sorteados in todos_numeros:
		contador = 0
		for numero_escolhido in lista_numeros_escolhidos:
			if numero_escolhido in numeros_sorteados:
				print(numeros_sorteados)
				contador+= 1
		print(contador)

if __name__ == '__main__':
	popula_numeros()
	#print(todos_numeros)



#print(contador)

#loto.printValues(todos_numeros)

#datasets = loto.createListNumber()
