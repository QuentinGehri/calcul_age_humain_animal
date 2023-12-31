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

    def test_age_humain_0an_chien_trop_jeune_fonctionnel(self):
        date_str = "10.05.2023"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chien(ma_date, 'Marley')
        self.assertEqual("Trop jeune pour qu'on puisse estimer son âge", marley.age_humain())

    def test_age_humain_1an_age_chien_15ans_fonctionnel(self):
        date_str = "10.05.2022"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chien(ma_date, 'Marley')
        self.assertEqual(15, marley.age_humain())

    def test_age_humain_2ans_age_chien_24ans_fonctionnel(self):
        date_str = "10.05.2021"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chien(ma_date, 'Marley')
        self.assertEqual(24, marley.age_humain())

    def test_age_humain_3ans_age_chien_29ans_fonctionnel(self):
        date_str = "10.05.2020"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chien(ma_date, 'Marley')
        self.assertEqual(29, marley.age_humain())

    def test_age_humain_5ans_age_chien_39ans_fonctionnel(self):
        date_str = "10.05.2018"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chien(ma_date, 'Marley')
        self.assertEqual(39, marley.age_humain())

    def test_age_humain_10ans_age_chien_64ans_fonctionnel(self):
        date_str = "10.05.2013"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chien(ma_date, 'Marley')
        self.assertEqual(64, marley.age_humain())

    # Chat
    def test_str_chat_fonctionnel(self):
        date_str = "19.12.2023"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual("Je suis un chat du nom de Marley, né le 19.12.2023", marley.__str__())

    def test_age_humain_0an_chat_trop_jeune_fonctionnel(self):
        date_str = "10.05.2023"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual("Trop jeune pour qu'on puisse estimer son âge", marley.age_humain())

    def test_age_humain_1an_age_chat_15ans_fonctionnel(self):
        date_str = "10.05.2022"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual(15, marley.age_humain())

    def test_age_humain_2an_age_chat_24ans_fonctionnel(self):
        date_str = "10.05.2021"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual(24, marley.age_humain())

    def test_age_humain_3an_age_chat_28ans_fonctionnel(self):
        date_str = "10.05.2020"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual(28, marley.age_humain())

    def test_age_humain_4an_age_chat_32ans_fonctionnel(self):
        date_str = "10.05.2019"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual(32, marley.age_humain())

    def test_age_humain_10an_age_chat_56ans_fonctionnel(self):
        date_str = "10.05.2013"
        date_format = "%d.%m.%Y"
        ma_date = datetime.strptime(date_str, date_format)
        marley = Chat(ma_date, 'Marley')
        self.assertEqual(56, marley.age_humain())


if __name__ == '__main__':
    unittest.main()
