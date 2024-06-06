'''
Title:
    modificar_frames

Description:
    Crea un total de 6 archivos evaluando un archivo FASTA, donde cada 
    archivo contiene los codones de sus secuencias separados por 
    espacios seg�n sea su marco de lectura.

Usage:
    python crear_frames.py <input_file> -n <marcos>
Args:
    archivo: La ruta del archivo que contiene la cadena de ADN a analizar
Method:
1. Se parsea el archivo FASTA dado por el usuario al llamar al programa.
2. Se llama a la funci�n crear_frames con el archivo parseado y guardado en una variable.
3. La funcion hace un bucle para crear un archivo donde establece su titulo segun el marco de lectura.
4. Se abre un bucle anidado que asigna a la variable seq_str_forward la secuencia segun su id en el archivo.
5. Se abre otro bucle anidado que separa los codones de la cadena cambiando su inicio en i para cambiar el marco.
6. Se realizan los mismos pasos del 3 al 5 con la diferencia que invierte la cadena para el resto de marcos.
'''
#===========================================================================
#=================================Imports===================================
#import sys
import argparse
#sys.path.append('C:/Users/phoen/OneDrive/Escritorio/pruebas_bp/carpeta_modulos/operations')
from modulos.operations.dogma import transcripcion, traduccion 
from modulos.operations.ids_seq import parseo
#===========================================================================

# ===========================================================================
# ================================Functions===================================
parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida")
parser.add_argument("inputs_files", type=str, nargs='+', help="El archivo de texto que quieres procesar.")
parser.add_argument('-t','--tipo', type=str, choices=['R', 'P', 'RP'],default='R',
                    help="Indicar que tipo trandormacion quieres hacerle a la secuencia si a RNA(R), a proteinas(p) o ambas(RP)") 

args = parser.parse_args()

def procesar_frame(tipo_modif, inputs_files):
    if tipo_modif == 'R' or tipo_modif == 'RP' :
        for i, frames in enumerate(inputs_files):
            Datos = parseo(frames)
            with open(f'RNA_{i+1}.txt', 'w') as archivos:
                for id, seq in Datos.items():
                    archivos.write(">{}\n".format(id))
                    archivos.write("{}\n".format(transcripcion(seq)))

    if tipo_modif == 'P' or tipo_modif == 'RP':
        for i, frames in enumerate(inputs_files):
            Datos = parseo(frames)
            with open(f'Proteinas_{i+1}.txt', 'w') as archivos:
                for id, seq in Datos.items():
                    archivos.write(">{}\n".format(id))
                    archivos.write("{}\n".format(traduccion(seq)))

procesar_frame(args.tipo, args.inputs_files)
