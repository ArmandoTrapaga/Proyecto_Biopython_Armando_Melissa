# dogma 

Fecha: 05/06/2024

**Participantes**:
- Armando Gael Gonzalez <email:aggonzal@lcg.unam.mx>
- Melissa Palma <email:melissap@lcg.unam.mx>

## Descripcion del Problema
    Este script realiza la transcripcion y traduccion de una secuencia de ADN en una secuencia de ARN
    y luego en una secuencia de peptidos, respectivamente.

## Especificacion de Requisitos

Requisitos funcionales

Requisitos no funcionales

## Analisis y Diseno
El script dogma.py es un modulo de Python para realizar la transcripcion y traduccion de una secuencia de ADN en una secuencia de ARN, y luego en una secuencia de peptidos, respectivamente. Comienza definiendo dos diccionarios: uno para las bases complementarias del ARN y otro para el codigo genetico que mapea tripletes de ARN a aminoacidos. La funcion transcripcion toma una secuencia de ADN como entrada y la transcribe en ARN, reemplazando las bases correspondientes segun las reglas de complementariedad. La funcion traduccion toma una secuencia de ARN, transcribe sus tripletes en aminoacidos segun el codigo genetico, comenzando desde el codón de inicio AUG y terminando en el codon de terminación UGA. Ambas funciones operan eliminando los espacios en la secuencia de ARN resultante antes de su procesamiento. Finalmente, en la seccion __name__ == '__main__', se proporciona una secuencia de ADN de ejemplo, se transcribe en ARN y luego se traduce en una secuencia de peptidos, mostrando los resultados en la consola.
```
# imports
import re

# Diccionario para bases complementarias del ARN
bases_complementarias_RNA = {
    'A': 'A', 'T': 'U', 'C': 'C', 'G': 'G',}

# Diccionario del codigo genetico
codigo_genetico = {  
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UGU': 'C', 'UGC': 'C', 'UGA': '-', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

def transcripcion(secuencia):
    """
    Transcribe una secuencia de ADN en una secuencia de ARN.
   
    Args:
        secuencia (str): La secuencia de ADN a transcribir.
       
    Returns:
        str: La secuencia de ARN transcrita.
    """
    transcrito = ''
    # Eliminar espacios en la secuencia de ADN
    secuencia = secuencia.replace(" ", "")
    # Iterar sobre cada nucleotido en la secuencia de ADN
    for i, nucleotido in enumerate(secuencia):
        if nucleotido not in bases_complementarias_RNA:
            continue
        transcrito += bases_complementarias_RNA[nucleotido]
        if (i+1) % 3 == 0:
            transcrito += ' '
            i -= 1
    return transcrito


def traduccion(secuencia):
    """
    Traduce una secuencia de ARN en una secuencia de peptidos.
   
    Args:
        secuencia (str): La secuencia de ARN a traducir.
       
    Returns:
        str: La secuencia de peptidos traducida.
    """
    peptido = ''
    # Eliminar espacios en la secuencia de RNA
    secuencia = transcripcion(secuencia)
    # Buscar el codon de inicio (AUG)
    inicio = secuencia.find('AUG')
    if inicio!= -1:
        # Iniciar la traduccion desde el codon de inicio
        posicion_actual = inicio
        while True:
            # Dividir la secuencia en codones (tripletes)
            for codon in re.findall(r"(.{3})", secuencia[posicion_actual:]):
                # Detener la traduccion al encontrar el codon de terminacion (UGA)
                if codon == 'UGA':
                    peptido += ' '
                    break
                # Verificar si el codon está en el diccionario del codigo genetico
                if codon not in codigo_genetico:
                    continue
                # Se agrega aminoacido correspondiente al peptido
                peptido += codigo_genetico[codon]
                posicion_actual += 3
            else:
                break  # No hay mas codones, salir del bucle interno
            inicio = secuencia.find('AUG', posicion_actual)  # Buscar el siguiente AUG
            if inicio == -1:
                break  # No se encuentra mas AUG, salir del bucle externo
            posicion_actual = inicio
    return peptido


if __name__ == '__main__':
    seq = 'ATGCTTCTTCTTTGAATATAATGCTTCTTCTTTGA'
    # Transcribir la secuencia de ADN a ARN
    seq_RNA = traduccion(seq)
    print(seq_RNA)
    # Traducir la secuencia de ARN a peptidos
    seq_pep = traduccion(seq)
    print(seq_pep)
```
#### Caso de uso: 
```
+---------------+
|   Usuario     |
+-------+-------+
        |
        | Proporciona una secuencia de ADN
        v
+---------------+
|   Programa    |
|               |
|               |
|               |
+-------+-------+
        |
        | 1. Transcribe la secuencia de ADN a ARN
        v
+---------------+
|   transcripcion() |
|   (secuencia)    |
+-------+-------+
        |
        | 2. Traduce la secuencia de ARN a péptidos
        v
+---------------+
|   traduccion()  |
|   (secuencia)  |
+-------+-------+
        |
        | 3. Imprime la secuencia de ARN y péptidos
        v
+---------------+
|   Imprimir    |
|   resultados  |
+---------------+

```
- **Actor**: Usuario
- **Descripcion**: La persona que ejecuta el script y proporciona la secuencia de ADN como entrada. 
- **Flujo de eventos principal:**
Flujo de Eventos:
    1. El Usuario ejecuta el script dogma.py.
    2. El Usuario proporciona una secuencia de ADN como entrada.
    3. El script transcribe la secuencia de ADN en una secuencia de ARN.
    4. El script traduce la secuencia de ARN en una secuencia de péptidos utilizando el código genético estándar.
    5. El script muestra la secuencia de ARN transcrita y la secuencia de péptidos traducida al Usuario.
**Escenarios Alternativos:**
    - Si la secuencia de ADN proporcionada por el Usuario contiene caracteres que no son A, T, C o G, el script ignora esos caracteres y continúa con la transcripción y traducción.
    - Si la secuencia de ARN generada durante la transcripción no contiene el codón de inicio AUG, el script no produce una secuencia de péptidos.