#!/usr/bin/python
from bs4 import BeautifulSoup

arquivo = None
soup = None

path = './D_LOTFAC.HTM'

def findValueTD(row):
	return [td.get_text() for td in row.find_all("td")]

def findNumber(numberList):
	return [int(numberList[indice]) for indice in range(2, 17)]

def printValues(dados):
	[print(valor) for valor in dados]

# The first tr contains the field names.
#headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]
def createListNumber():
	arquivo = open(path, 'r')
	soup = BeautifulSoup(arquivo.read(), "html.parser")
	table = soup.find("table")
	datasets = []
	for row in table.find_all("tr"):
		dataset = findValueTD(row)
		if len(dataset) > 18:
			datasets.append(findNumber(dataset))

	arquivo.close()
	return datasets

#printValues(createListNumber())