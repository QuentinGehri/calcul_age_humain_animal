from datetime import datetime


class Animal:
    def __init__(self, date_anniv, nom):
        self.date_anniv = date_anniv
        self.nom = nom

    def calculer_age(self):
        date_actuelle = datetime.now()
        date_naissance = self.date_anniv
        age = date_actuelle.year - date_naissance.year
        if (date_actuelle.month, date_actuelle.day) < (date_naissance.month, date_naissance.day):
            age -= 1
        return age

    def age_humain(self):
        pass

    def __str__(self, type_animal="animal"):
        date_formatee = self.date_anniv.strftime("%d.%m.%Y")
        return f"Je suis un {type_animal} du nom de {self.nom}, né le {date_formatee}"

