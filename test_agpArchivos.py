""" ***********************************************************************************************
AgroPerception
Autor: JRCR
Compilador: Python 3.6
Editor: Sublime Text
Fecha: 08/01/2017
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
archivo = ""
class TestAgpArchivos(unittest.TestCase):

    def test_verificaArchivo(self):
        global archivo
        self.assertEqual(agpArchivos.verificaArchivo(archivo), True)

    def test_cuentaPalabas(self):
        global archivo
        self.assertEqual(agpArchivos.cuentaPalabras(archivo), 11)

    def test_cuentaLetras(self):
        global archivo
        self.assertEqual(agpArchivos.cuentaLetras(archivo), 39)

"""------------------------------------------------------------------------------------------------
									main
- Ejecución de prueb unitaria
------------------------------------------------------------------------------------------------"""
if __name__ == "__main__":
    archivo = input("Ingrese path del archivo: ").strip()
    unittest.main() 

#>>>>>>>>>> Fin de archivo: test_agpArchivos.py <<<<<<<<<<
	