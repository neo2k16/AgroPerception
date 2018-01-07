""" ***********************************************************************************************
AgroPerception
Autor: JRCR
Compilador: Python 3.6
Editor: Sublime Text
Fecha: 05/01/2017
Archivo: agpArchivos.py
Programa: 
	Lectura desde un archivo. 
	Entrega número de palabras y letras.
	Estándard de codificación pep8
	Incluye pruebas unitarias en archivo: test_agpArchivos.py
*********************************************************************************************** """ 
"""------------------------------------------------------------------------------------------------
										import
------------------------------------------------------------------------------------------------"""
import os.path
from io import open

"""------------------------------------------------------------------------------------------------
										verficaArchivo
	- Verifica existencia de Archivo
------------------------------------------------------------------------------------------------"""
def verificaArchivo(archivo):
	return (os.path.isfile(archivo))

"""------------------------------------------------------------------------------------------------
										cuentaPalabras
	- Elimina caracteres especiales y signos de puntuación										
------------------------------------------------------------------------------------------------"""
def cuentaPalabras(archivo):
	if (verificaArchivo(archivo) == False):
		print("El archivo no existe")
		return -1;

	nLineas, nPalabras = 0,0

	archivoTexto = open (archivo, "r", encoding="utf-8")
	for line in archivoTexto:
		listaPalabras = line.replace(',','').replace('.','').replace('\n',' ').replace('\r',' ').replace('\t',' ').replace('  ', ' ').lower().split()
		nLineas += 1
		nPalabras += len(listaPalabras)
	archivoTexto.close()

	return nPalabras

"""------------------------------------------------------------------------------------------------
										cuentaLetras
	- Recorre el archivo caracter por caracter
	- Utiliza diccionarios de vocales, consonantes y dígitos										
------------------------------------------------------------------------------------------------"""
def cuentaLetras(archivo):
	if (verificaArchivo(archivo) == False):
		print("El archivo no existe")
		return -1;

	nVocales, nConsonantes, nLetras, nDigitos, nCaracteres = 0,0,0,0,0
	vocales = set("AEIOUaeiouÁÉÍÓÚáéíóú")
	consonantes = set("bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ")
	digitos = set("0123456789")

	archivoTexto = open (archivo, "r", encoding="utf-8")
	for c in archivoTexto.read():
		nCaracteres += 1
		if c in vocales:
			nVocales += 1
		elif c in consonantes:
			nConsonantes += 1
		elif c in digitos:
			nDigitos += 1	
	archivoTexto.close()
	nLetras = nVocales + nConsonantes
	return nLetras

"""------------------------------------------------------------------------------------------------
										main
	- Función principal
------------------------------------------------------------------------------------------------"""
def main():
	#archivo = input("Ingrese Archivo: ").strip()

	archivo = "archivo.txt"
	
	if (verificaArchivo(archivo) == False):
		print("El archivo no existe")
		return;

	nPalabras = cuentaPalabras(archivo)
	print ("nPalabras: " + str(nPalabras))
		
	nLetras = cuentaLetras(archivo)
	print ("nLetras: " + str(nLetras))

main()

#>>>>>>>>>> Fin de Archivo: agpArchivos.py <<<<<<<<<<
