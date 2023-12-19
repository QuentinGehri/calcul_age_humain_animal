class Animal:
    def __init__(self, date_anniv, nom):
        self.date_anniv = date_anniv
        self.nom = nom

    def __str__(self):
        date_formatee = self.date_anniv.strftime("%d-%m-%Y")
        return f"Je suis un animal du nom de {self.nom}, né le {date_formatee}"