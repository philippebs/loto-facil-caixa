#!/usr/bin/python
import requests, zipfile, os

def download_descompactar():
	BASE_PATH = os.path.dirname(os.path.abspath(__file__))
	print(BASE_PATH)

	request = requests.get('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip')
	with open('D_lotfac.zip', 'wb') as code:
		code.write(request.content)

	zip = zipfile.ZipFile(BASE_PATH + '/D_lotfac.zip')
	#zip.write(BASE_PATH, compress_type=zipfile.ZIP_DEFLATED)
	
	zip.extractall(BASE_PATH)
	zip.close()
	

if __name__ == '__main__':
	download_descompactar();