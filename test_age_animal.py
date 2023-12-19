import unittest
from datetime import datetime
from Animal import Animal


class MyTestCase(unittest.TestCase):
    def test_est_un_animal(self):
        date_str = "2023-12-19"
        date_format = "%Y-%m-%d"
        ma_date = datetime.strptime(date_str, date_format)
        self.assertEqual("Je suis un animal du nom de Marley", Animal(ma_date, 'Marley'))  # add assertion here


if __name__ == '__main__':
    unittest.main()
