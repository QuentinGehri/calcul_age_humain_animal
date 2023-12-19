import unittest
from datetime import datetime
from Animal import Animal


class MyTestCase(unittest.TestCase):
    def test_str_fonctionnel(self):
        date_str = "19-12-2023"
        date_format = "%d-%m-%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Animal(ma_date, 'Marley')
        self.assertEqual("Je suis un animal du nom de Marley, né le 19-12-2023", marley.__str__())  # add assertion here


if __name__ == '__main__':
    unittest.main()
