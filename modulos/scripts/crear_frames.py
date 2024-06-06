'''
Title: 
    Crear_frames    

Description

Crea un total de 6 archivos evaluando un archivo fasta, donde cada archivo contiene los codones de sus secuencias 
separados por espacios segun sea su marco de lectura

Usage
    python crear_frames.py

Args:
- archivo: La ruta del archivo que contiene la cadena de ADN a analizar.

Method:
1.- Se parsea el archivo fasta dado por el usario al llamar al programa
2.- Se llama la funcion crear_frames con el archivo parseado y guardado en una variable 
3.- La funcion hace un for para crear un archivo donde establece su titulo segun el marco de lectura  
4.- Se abre un for anidado que asigna a la variable seq_str_forward la secuencia segun su id en el archivo
5.- Se abre otro for anidado que separa los condones de la cadena cambiando su inicio en i para cambiar el marco
6.- Se realiza los mismos pasos del 3 al 5 con la diferencia que invierte la cadena para el resto de marcos
'''
#===========================================================================
#=================================Imports===================================
import re
import argparse
# import sys
# sys.path.append('C:/Users/phoen/OneDrive/Escritorio/pruebas_bp/carpeta_modulos/operations')
from modulos.operations.ids_seq import parseo
#============================================================================

# ===========================================================================
# ================================Functions===================================

# Creamos un objeto ArgumentParser para manejar los argumentos de linea de comandos
parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida")

# Agregamos un argumento obligatorio para el archivo de entrada
parser.add_argument("input_file", type=str, help="El archivo de texto que quieres procesar.")
# Agregamos un argumento opcional para los marcos de lectura
parser.add_argument('-n', "--marcos", type=str, nargs="+",default="1", help="El marco de lectura que quieres conseguir")

# Parseamos los argumentos proporcionados por el usuario
args = parser.parse_args()

# Asignamos el parseo a una variable del main
archivo_seq = args.input_file

marcos = [int(num) for num in args.marcos if int(num) <= 6 and int(num) >=1]

# Definimos una clase para manejar los marcos de lectura
class frames():
    def __init__(self,archivo, marcos):
        self.archivo = archivo
        self.marcos = marcos
    

    def crear_frames(self):
        try:
            for i in marcos:
                #Se establece el titulo i + 1 
                Datos = {}
                with open(f"Frame_{i}.txt", "w") as file_forward:
                    # Parseamos el archivo de entrada
                    Datos = parseo(self.archivo)
                    for ids, seqs in Datos.items():
                        file_forward.write(">{}\n".format(ids))
                        if i <4:
                            # Procesa los marcos de lectura directos
                            for condon in re.findall(r"(.{3})", seqs[(i-1):]):
                                file_forward.write(condon + " ")
                            file_forward.write("\n")
                        else:
                            # Procesa los marcos de lectura inversos
                            seq_str_reverse = seqs[::-1]
                            for codon in re.findall(r"(.{3})", seq_str_reverse[(i-4):]):
                                file_forward.write(codon + " ")
                            file_forward.write("\n")
        except IOError:
            print("IOERROR: No se pudo abrir el archivo. Por favor, asegúrate de que el archivo existe y que has proporcionado la ruta correcta.")        
        

#=========================================================================
#============================Main=========================================
#Se llama a la funcion
ejemplo = frames(archivo_seq, marcos)
ejemplo.crear_frames()
#=========================================================================