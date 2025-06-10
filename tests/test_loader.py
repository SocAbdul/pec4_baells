import unittest
from src.exercises.ex5_sequias import calcula_periodos

class TestSequias(unittest.TestCase):
    def test_calcula_periodos(self):
        """
        Test para la función `calcula_periodos`.

        Comprueba si la función detecta correctamente un único periodo de sequía 
        en una serie simple de datos. El umbral utilizado es 60, y se espera que 
        se detecte el periodo entre 2000.5 y 2001.5.
        """
        x = [2000.0, 2000.5, 2001.0, 2001.5, 2002.0]
        y = [70, 55, 50, 65, 75]
        expected = [[2000.5, 2001.5]]
        result = calcula_periodos(x, y, umbral=60)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
