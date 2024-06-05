import re
bases_complementarias_RNA = {
    'A': 'A', 'T': 'U', 'C': 'C', 'G': 'G',}

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
    transcrito = ''
    secuencia = secuencia.replace(" ", "")
    for i, nucleotido in enumerate(secuencia):
        if nucleotido not in bases_complementarias_RNA:
            continue
        transcrito += bases_complementarias_RNA[nucleotido]
        if (i+1) % 3 == 0:
            transcrito += ' '
            i -= 1 
    return transcrito

def traduccion(secuencia):
    peptido = ''
    secuencia = transcripcion(secuencia)
    inicio = secuencia.find('AUG')
    if inicio!= -1:
        posicion_actual = inicio
        while True:
            for codon in re.findall(r"(.{3})", secuencia[posicion_actual:]):
                if codon == 'UGA':
                    peptido += ' '
                    break
                if codon not in codigo_genetico:
                    continue
                peptido += codigo_genetico[codon]
                posicion_actual += 3
            else:
                break  # No hay más codones, salir del bucle interno
            inicio = secuencia.find('AUG', posicion_actual)  # Buscar el siguiente AUG
            if inicio == -1:
                break  # No se encuentra más AUG, salir del bucle externo
            posicion_actual = inicio
    return peptido

 
seq = 'ATGCTTCTTCTTTGAATATAATGCTTCTTCTTTGA'
seq = traduccion(seq)
print(seq)