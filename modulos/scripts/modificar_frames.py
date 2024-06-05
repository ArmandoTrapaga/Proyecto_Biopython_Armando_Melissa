#import sys
import argparse
#sys.path.append('C:/Users/phoen/OneDrive/Escritorio/pruebas_bp/carpeta_modulos/operations')
from modulos.operations.dogma import transcripcion, traduccion 
from modulos.operations.ids_seq import parseo

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


