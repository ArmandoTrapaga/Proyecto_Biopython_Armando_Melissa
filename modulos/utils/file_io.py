"""

file_io.py: Funciones para manejar operaciones de entrada/salida de archivos de ADN.

Este módulo provee funcionalidades para leer y escribir secuencias de ADN desde y hacia
archivos, asegurando que las secuencias sean válidas y estén bien formateadas.

Funciones:
    read_dna_sequence(filename) - Lee una secuencia de ADN de un archivo.
    write_dna_sequence(filename, sequence) - Escribe una secuencia de ADN en un archivo.
    
Ejemplos de uso estan disponibles en el bloque principal del modulo.

Autores: [Tu Nombre]
Versión: 1.0
"""

# imports

# meta-info
_author_ = "Tu Nombre"
_version_ = "1.0"

# global vars

# functions internal

# main functions

def read_dna_sequence(filename):
    """
    Lee el archivo dado y verifica si tiene formato fasta, en caso de ser texto lo pasa a fasta
    
    Args:
        filename (str): El nombre del archivo del cual leer la secuencia.
        
    Returns:
        str: El archivo fasta original
        str: El archivo texto vuelto fasta
        
    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
        ValueError: Si el archivo está vacío o contiene caracteres no válidos.
    """
    try:
        with open(filename, 'r') as file:
            if not file.read.strip():
                raise ValueError('El archivo esta vacio')            
            if file.startswith('>'):
                return filename
            if any(char not in 'ACGT' for char in file.read().upper().strip()):
                raise ValueError('La secuencia contiene caracteres no validos')    
            return write_dna_sequence(filename)
    except FileNotFoundError:
        print(f"El archivo {filename} no fue encontrado.")
        return 


def write_dna_sequence(filename):
    """
    Escribe una secuencia de ADN en un archivo de texto.
    
    Args:
        filename (str): El nombre del archivo donde se escribirá la secuencia.
        sequence (str): La secuencia de ADN a escribir.
        
    Raises:
        IOError: Si no se puede escribir en el archivo.
    """
    with open(filename, 'r') as file:
        texto = file.read().upper().strip()

    i = 1
    contador_saltos = 0
    with open('fasta', 'w') as creado: 
        creado.write(f'>seq{i}\n')
        i += 1 
        for linea in texto:
            if linea == '\n':
                contador_saltos += 1
            else:
                if contador_saltos > 1:
                    creado.write(f'\n>seq{i}\n')
                    i += 1
                contador_saltos = 0
                creado.write(linea)

if _name_ == "_main_":
    # Bloques de prueba para demostrar la funcionalidad del módulo.
    
    # Suponiendo que el archivo "example_dna.txt" contiene la secuencia válida "ATCG"
    try:
        sequence = read_dna_sequence("example_dna.txt")
        print(f"Secuencia leída correctamente: {sequence}")
        
        # Ahora escribir esta secuencia a un nuevo archivo
        write_dna_sequence("output_dna.txt", sequence)
        print("Secuencia escrita correctamente en 'output_dna.txt'.")
    except Exception as e:
        print(f"Error: {str(e)}")