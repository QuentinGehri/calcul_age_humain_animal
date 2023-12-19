import unittest
from datetime import datetime
from Animal import Animal
from Chien import Chien
from Chat import Chat


class MyTestCase(unittest.TestCase):
    # Animal
    def test_str_animal_fonctionnel(self):
        date_str = "19.12.2023"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Animal(ma_date, 'Marley')
        self.assertEqual("Je suis un animal du nom de Marley, né le 19.12.2023", marley.__str__())

    def test_calculer_age_1an_animal(self):
        date_str = "10.12.2022"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Animal(ma_date, 'Marley')
        self.assertEqual(1, marley.calculer_age())

    def test_calculer_age_0an_animal(self):
        date_str = "20.12.2022"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Animal(ma_date, 'Marley')
        self.assertEqual(0, marley.calculer_age())

    def test_calculer_age_5an_animal(self):
        date_str = "10.12.2018"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Animal(ma_date, 'Marley')
        self.assertEqual(5, marley.calculer_age())

    # Chien
    def test_str_chien_fonctionnel(self):
        date_str = "19.12.2023"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chien(ma_date, 'Marley')
        self.assertEqual("Je suis un chien du nom de Marley, né le 19.12.2023", marley.__str__())

    # Chat
    def test_str_chat_fonctionnel(self):
        date_str = "19.12.2023"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual("Je suis un chat du nom de Marley, né le 19.12.2023", marley.__str__())


if __name__ == '__main__':
    unittest.main()
