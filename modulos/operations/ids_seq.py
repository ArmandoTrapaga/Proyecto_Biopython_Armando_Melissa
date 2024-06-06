"""
    Title:
        ids_seq.py
    Usage:
        Python ids_seq.py
        
    Descripcion:
        Este modulo proporciona una funcion para parsear archivos en formato FASTA.
        La funcion lee un archivo FASTA y convierte las secuencias en un diccionario 
        donde las claves son los IDs de los registros y los valores son las secuencias
        de ADN asociadas.
        
    Funciones:
        parseo(file_path) - Lee un archivo FASTA y devuelve un diccionario con los IDs y las secuencias.
"""

def parseo(file_path):
    Datos = {}
    # Abre el archivo FASTA para lectura
    
    with open(file_path, 'r') as fasta_file:
        """
    Lee un archivo FASTA y devuelve un diccionario con los IDs y las secuencias.

    Args:
        file_path (str): La ruta del archivo FASTA a leer.

    Returns:
        dict: Un diccionario donde las claves son los IDs de los registros y 
        los valores son las secuencias de ADN asociadas.
    """
        registro_id = None
        secuencia = []
        
        # Itera sobre cada linea del archivo
        for line in fasta_file:
            if line.startswith('>'):
                # Si encuentra una nueva cabecera, guarda la secuencia previa
                if registro_id is not None:
                    Datos[registro_id] = ''.join(secuencia)
                    # Actualiza el ID del registro actual y limpia la secuencia
                registro_id = line.strip()[1:]  # Elimina el '>' y espacios adicionales
                secuencia.clear()
            else:
                # Agrega la linea de secuencia al registro actual
                secuencia.append(line.strip())
        
        # Guarda la ultima secuencia procesada
        if registro_id is not None:
            Datos[registro_id] = ''.join(secuencia)
    
    return Datos

if __name__ == '__main__':
    with open('archivo_main_ids_seq.txt', 'w') as file:
        file.write('>seq1\nATGCTTCTTCTTTGAATATAATGCTTCTTCTTTGA')
    # Llama a la funcion parseo y imprime el resultado
    print(parseo('archivo_main_ids_seq.txt'))