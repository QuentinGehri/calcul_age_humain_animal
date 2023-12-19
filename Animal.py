class Animal:
    def __init__(self, date_anniv, nom):
        self.date_anniv = date_anniv
        self.nom = nom

    def calculer_age(self):
        pass

    def age_humain(self):
        pass

    def __str__(self, type_animal="animal"):
        date_formatee = self.date_anniv.strftime("%d.%m.%Y")
        return f"Je suis un {type_animal} du nom de {self.nom}, né le {date_formatee}"

