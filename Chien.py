from Animal import Animal


class Chien(Animal):
    def __init__(self, date_anniv, nom):
        super().__init__(date_anniv, nom)

    def age_humain(self):
        pass

    def __str__(self):
        date_formatee = self.date_anniv.strftime("%d.%m.%Y")
        return f"Je suis un chien du nom de {self.nom}, né le {date_formatee}"
