""" ***********************************************************************************************
AgroPerception
Autor: JRCR
Compilador: Python 3.6
Editor: Sublime Text
Fecha: 06/01/2017
Archivo: test_agpArchivos.py
Programa: 
	Pruebas unitarias del programa agpArchivos.py 
	Archivo de prueba: "archivo.txt": 
		- Palabras: 11
		- Letras: 39
*********************************************************************************************** """
"""------------------------------------------------------------------------------------------------
										import
------------------------------------------------------------------------------------------------"""
import unittest
import agpArchivos

"""------------------------------------------------------------------------------------------------
									class TestAgpArchivos
------------------------------------------------------------------------------------------------"""

class TestAgpArchivos(unittest.TestCase):
	def test_verificaArchivo(self):
		self.assertEqual(agpArchivos.verificaArchivo("archivo.txt"), True)

	def test_cuentaPalabas(self):
		self.assertEqual(agpArchivos.cuentaPalabras("archivo.txt"), 11)

	def test_cuentaLetras(self):
		self.assertEqual(agpArchivos.cuentaLetras("archivo.txt"), 39)

"""------------------------------------------------------------------------------------------------
									main
- Ejecución de prueb unitaria
------------------------------------------------------------------------------------------------"""
if __name__ == "__main__":
	unittest.main() 

#>>>>>>>>>> Fin de archivo: test_agpArchivos.py <<<<<<<<<<
	