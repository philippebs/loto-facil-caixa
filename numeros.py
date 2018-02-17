#!/usr/bin/python
import loto

todos_numeros = []

def popula_numeros():
	todos_numeros = loto.createListNumber()

def rastreio_numeros(lista_numeros_escolhidos):
	
	for numeros_sorteados in todos_numeros:
		contador = 0
		for numero_escolhido in lista_numeros_escolhidos:
			if numero_escolhido in numeros_sorteados:
				contador+= 1
		print(contador)
		break





#print(contador)

#loto.printValues(todos_numeros)

#datasets = loto.createListNumber()
