# complemento

Fecha: 05/06/2024

**Participantes**:
- Armando Gael Gonzalez <email:aggonzal@lcg.unam.mx>
- Melissa Palma <email:melissap@lcg.unam.mx>

## Descripcion del Problema

    Este modulo de Python proporciona funciones para calcular el complemento de una secuencia de nucleotidos de ARN o DNA. Utiliza diccionarios predefinidos para encontrar los pares complementarios de nucleotidos  y generar la secuencia complementaria.

## Especificacion de Requisitos

**Requisitos funcionales:**
   - El modulo debe proporcionar funciones para calcular el complemento de una secuencia de nucleotidos de ARN (complemento_RNA) y de ADN (complemento_DNA).
    - El modulo debe aceptar secuencias de nucleotidos de ARN o ADN como entrada.
    - El modulo debe devolver la secuencia complementaria como salida después de calcularla.

## Analisis y Diseno

El modilo contiene dos funciones principales: complemento_DNA y complemento_RNA. Estas funciones calculan el complemento de una secuencia de nucleotidos de ADN o ARN, respectivamente, utilizando diccionarios predefinidos que contienen las bases complementarias para ADN y ARN. El programa tambien incluye un bloque condicional que permite ejecutar algunas demostraciones de las funciones cuando el archivo se ejecuta como un script independiente. En este caso, se proporciona una secuencia de nucleotidos de ARN, se calcula su complemento de ARN y se imprime en la salida estándar. Luego, se calcula el complemento de la secuencia de ADN y se almacena en una variable, pero no se imprime. El codigo está bien estructurado y documentado, facilitando su comprension y uso.

```
# Diccionarios que contienen las bases complementarias para ADN y ARN
bases_complementarias_DNA = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
}
bases_complementarias_RNA = {
    'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C',
}

def complemento_DNA(secuencia):
    """Calcula el complemento de una secuencia de nucleotidos de DNA.

    Args:
        secuencia (str): La secuencia de nucleotidos de ADN a la que se le
        calculara el complemento.

    Returns:
        str: Secuencia complementaria de nucleotidos de DNA.
    """
    complemento = ''
    for nucleotido in secuencia:
        # Se busca el complemento en el diccionario de bases complementarias de DNA
        complemento += bases_complementarias_DNA[nucleotido]
    return complemento

def complemento_RNA(secuencia):
    """Calcula el complemento de una secuencia de nucleotidos de RNA.

    Args:
        secuencia (str): La secuencia de nucleotidos de ARN a la que se le calculara
        el complemento.

    Returns:
        str: La secuencia complementaria de nucleotidos de ARN.
    """
    complemento = ''
    for nucleotido in secuencia:
        # Se busca el complemento en el diccionario de bases complementarias de RNA
        complemento += bases_complementarias_RNA[nucleotido]
    return complemento

if __name__ == '__main__':
    seq = 'ATGCTTCTTCTTTGAATATAATGCTTCTTCTTTGA'
    # Se calcula el complemento de la secuencia de RNA
    seq_com_rna = complemento_RNA(seq)
    print(seq_com_rna)
    # Se calcula el complemento de la secuencia de DNA
    seq_com_dna = complemento_DNA(seq)

```
#### Caso de uso: 
```
+---------------------+
| Inicio del programa|
+---------------------+
           |
           v
    Se define la
    secuencia de
    nucleótidos
           |
           v
    Se calcula el
    complemento de
    la secuencia de
    ARN utilizando
    la función
    complemento_RNA
           |
           v
    Se imprime el
    complemento de
    ARN
           |
           v
    Se calcula el
    complemento de
    la secuencia de
    ADN utilizando
    la función
    complemento_DNA
           |
           v
    Fin del programa
```
-**Actor**: Usuario
**Descripcion**: 
    - Este caso de uso describe el proceso de calcular el complemento de una secuencia de nucleotidos de ARN o ADN utilizando el modulo complemento.py.

**Flujo principal:**
    1. El usuario ejecuta el módulo complemento.py.
    2. El usuario proporciona una secuencia de nucleótidos de ARN o ADN como entrada.
    3. El sistema calcula el complemento de la secuencia utilizando las funciones complemento_RNA o complemento_DNA.
    4. El sistema devuelve la secuencia complementaria.
    5. El usuario recibe la secuencia complementaria como salida.

**Flujo alternativo:**

    - Si la entrada proporcionada por el usuario no es una secuencia válida de nucleotidos de ARN o ADN, el sistema muestra un mensaje de error y solicita al usuario que proporcione una entrada válida.
