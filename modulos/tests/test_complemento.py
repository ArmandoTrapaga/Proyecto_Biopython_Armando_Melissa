import unittest
from modulos.operations.complemento import complemento_DNA, complemento_RNA

class TestComplementoDNAyRNA(unittest.TestCase):

    def test_complemento_DNA(self):
        # Prueba para la función complemento_DNA
        secuencia = 'ATTGCCTCTCGTTAATATATAGCTTCGTAAGCTGAA'
        secuencia_esperada = 'TAACGGAGAGCAATTATATATCGAAGCATTCGACTT'
        self.assertEqual(complemento_DNA(secuencia), secuencia_esperada)

    def test_complemento_RNA(self):
        # Prueba para la función complemento_RNA
        secuencia = 'AUGCUUCUUCUUUGAAUAUAAUGCUUCUUCUUUGA'
        secuencia_esperada = 'UACGAAGAAGAAACUUAUAUUACGAAGAAGAAACU'
        self.assertEqual(complemento_RNA(secuencia), secuencia_esperada)

if __name__ == '__main__':
    unittest.main()