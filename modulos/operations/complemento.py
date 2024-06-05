"""_summary_

    Imports:
        none
"""

bases_complementarias_DNA = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
}
bases_complementarias_RNA = {
    'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C',
}
seq = 'AUCG'

def complemento_DNA(secuencia):
    complemento = ''
    for nucleotido in secuencia:
        complemento += bases_complementarias_DNA[nucleotido]
    return complemento

def complemento_RNA(secuencia):
    complemento = ''
    for nucleotido in secuencia:
        complemento += bases_complementarias_RNA[nucleotido]
    return complemento


seq = complemento_RNA(seq)
print(seq)