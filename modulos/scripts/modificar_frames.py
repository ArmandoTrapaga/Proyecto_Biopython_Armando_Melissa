import sys
import argparse
sys.path.append('C:/Users/phoen/OneDrive/Escritorio/pruebas_bp/carpeta_modulos/operations')
from dogma import transcripcion, traduccion 
from ids_seq import parseo

parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida")
parser.add_argument("inputs_files", type=str, nargs='+', help="El archivo de texto que quieres procesar.")
parser.add_argument('-t','--tipo', type=str, choices=['R', 'P', 'RP'],default='R',
                    help="Indicar que tipo trandormacion quieres hacerle a la secuencia si a RNA(R), a proteinas(p) o ambas(RP)") 

args = parser.parse_args()

if args.tipo == 'R' or args.tipo == 'RP' :
    for i, frames in enumerate(args.inputs_files):
        Datos = parseo(frames)
        with open(f'RNA_{i+1}.txt', 'w') as archivos:
            for id, seq in Datos.items():
                archivos.write(">{}\n".format(id))
                archivos.write("{}\n".format(transcripcion(seq)))

if args.tipo == 'P' or args.tipo == 'RP':
    for i, frames in enumerate(args.inputs_files):
        Datos = parseo(frames)
        with open(f'Proteinas_{i+1}.txt', 'w') as archivos:
            for id, seq in Datos.items():
                archivos.write(">{}\n".format(id))
                archivos.write("{}\n".format(traduccion(seq)))
     



