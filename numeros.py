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
				#print(numeros_sorteados)
				contador+= 1
		#print(contador)

def contar_vezes_que_aparece(numero):
	contador = 0
	for numero_sorteado in todos_numeros:
		if numero in numero_sorteado:
			contador+=1
	return contador

def calcular_porcentagem():
	numero = {valor : 0 for valor in range(1, 26)}
	for chave in numero:
		quantidade = contar_vezes_que_aparece(chave)
		numero[chave] = quantidade
		porcentagem = (quantidade * 100) / len(todos_numeros)
		print(str(chave) + ' - ' + str(porcentagem) + '%')

	[print(str(chave) + ' - ' + str(value)) for chave, value in numero.items()]

	#key = max(numero, key=numero.get)
	#quantidade = numero[key]

	#porcentagem = (quantidade * 100) / len(todos_numeros)

	#print('Maior quantidade de sorteios: ' + str(key) + ' - ' + str(quantidade) + ' : ' + str(porcentagem) + '%')

if __name__ == '__main__':
	popula_numeros()
	calcular_porcentagem()
	#print(todos_numeros)


#print(contador)
#loto.printValues(todos_numeros)
#datasets = loto.createListNumber()
