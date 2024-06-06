# ids_seq

Fecha: 05/06/2024

**Participantes**:
- Armando Gael Gonzalez <email:aggonzal@lcg.unam.mx>
- Melissa Palma <email:melissap@lcg.unam.mx>

## Descripcion del Problema
 Este modulo proporciona una funcion para parsear archivos en formato FASTA. La funcion lee un archivo FASTA y convierte las secuencias en un diccionario donde las claves son los IDs de los registros y los valores son las secuencias de ADN asociadas.

## Especificacion de Requisitos

Requisitos funcionales
    - La funcion debe ser capaz de leer un archivo en formato FASTA.
    - Debe convertir las secuencias del archivo en un diccionario donde las claves son los IDs de los registros y los valores son las secuencias de ADN asociadas.
    
## Analisis y Diseno

El codigo ids_seq.py implementa una funcion llamada parseo que permite analizar archivos en formato FASTA. Al recibir la ruta de un archivo FASTA, la funcion abre el archivo, lee línea por línea y extrae las secuencias de ADN junto con sus respectivos identificadores de registro. Estos datos se almacenan en un diccionario Python donde las claves son los IDs de los registros y los valores son las secuencias de ADN asociadas. Además, el bloque if __name__ == '__main__': se encarga de ejecutar un ejemplo de uso de la funcion parseo, creando un archivo de prueba con una secuencia de ADN y luego llamando a parseo con la ruta de este archivo para mostrar como funciona la funcion en la practica.
```
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
```
#### Caso de uso: 
```
+---------------+
|   Usuario     |
+-------+-------+
        |
        | 1. Proporciona archivo FASTA como entrada.
        v
+-------+-------+
|   Programa    |
|               |
|               |
|               |
+---------------+
        |
        | 2. Lee el archivo FASTA proporcionado.
        v
+---------------+
|   parseo()    |
|   (file_path) |
+-------+-------+
        |
        | 3. Abre el archivo FASTA para lectura.
        v
+---------------+
|   Lectura de  |
|   archivo     |
|   (fasta_file)|
+-------+-------+
        |
        | 4. Itera sobre cada linea del archivo.
        v
+---------------+
|   Procesamiento |
|   de cada linea |
|   (line)        |
+-------+-------+
        |
        | 5. Verifica si la linea comienza con '>'.
        |    Si es asi, guarda el ID del registro y prepara para almacenar la secuencia.
        |    Si no, agrega la línea a la secuencia del registro actual.
        v
+---------------+
|   Verificacion |
|   de cabecera  |
|   y agregado de|
|   línea        |
|   (line)       |
+-------+-------+
        |
        | 6. Continua procesando las líneas hasta el final del archivo.
        v
+---------------+
|   Fin del     |
|   archivo     |
|   (EOF)       |
+-------+-------+
        |
        | 7. Almacena la ultima secuencia procesada en el diccionario de datos.
        v
+---------------+
|   Almacenamiento |
|   de la secuencia|
|   (Datos)       |
+---------------+
        |
        | 8. Devuelve el diccionario de datos que contiene los IDs de los registros y las secuencias de ADN asociadas.
        v
+---------------+
|   Salida      |
|   (Datos)     |
+---------------+
```
- **Actor**: Usuario
- **Descripcion**: El actor proporciona un archivo 
- **Flujo de eventos principal:**

    1. El usuario llama a la función parseo y le pasa la ruta del archivo FASTA.
    2. La funcion parseo abre el archivo FASTA.
    3. La funcion lee cada linea del archivo.
    4. Si la linea comienza con '>', se reconoce como el ID de una secuencia.
    5. Las lineas siguientes se reconocen como la secuencia asociada hasta que se encuentra otro ID.
    6. La funcion almacena el ID y la secuencia en un diccionario.
    7. La funcion devuelve el diccionario al usuario.