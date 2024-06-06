import unittest
from modulos.operations.ids_seq import parseo

class TestComplementoDNAyRNA(unittest.TestCase):

    def test_parseo(self):
        with open('archivo_main_ids_seq.txt', 'w') as file:
            file.write('>seq1\nATGCTTCTTCTTTGAATATAATGCTTCTTCTTTGA')
        self.assertEqual(parseo('archivo_main_ids_seq.txt'), {'seq1': 'ATGCTTCTTCTTTGAATATAATGCTTCTTCTTTGA'})

if __name__ == '__main__':
    unittest.main()