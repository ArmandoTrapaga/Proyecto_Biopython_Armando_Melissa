import unittest
from modulos.operations.dogma import traduccion, transcripcion

class TestDogma(unittest.TestCase):

    def test_transcripcion(self):
        # Prueba para la función complemento_DNA
        secuencia = 'ATTGCCTCTCGTTAATATATAGCTTCGTAAGCTGAA'
        secuencia_esperada = 'AUU GCC UCU CGU UAA UAU AUA GCU UCG UAA GCU GAA '
        self.assertEqual(transcripcion(secuencia), secuencia_esperada)

    def test_traduccion(self):
        # Prueba para la función complemento_RNA
        secuencia = 'ATGCTTCTTCTTTGAATATAATGCTTCTTCTTTGA'
        secuencia_esperada = 'MLF'
        self.assertEqual(traduccion(secuencia), secuencia_esperada)

if __name__ == '__main__':
    unittest.main()