from Animal import Animal


class Chien(Animal):
    AGE_1AN = 15
    AGE_2AN = 24
    AJOUT_AGE_APRES_2AN = 5
    AGE_APRES_LEQUEL_ON_AJOUTE = 2

    def __init__(self, date_anniv, nom):
        super().__init__(date_anniv, nom)

    def age_humain(self):
        age = self.calculer_age()
        if age == 1:
            return self.AGE_1AN

    def __str__(self):
        return super().__str__("chien")
