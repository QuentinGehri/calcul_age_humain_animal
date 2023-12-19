from Animal import Animal


class Chat(Animal):
    AGE_1AN = 15
    AGE_2AN = 24
    AJOUT_AGE_APRES_2AN = 4
    AGE_APRES_LEQUEL_ON_AJOUTE = 2

    def __init__(self, date_anniv, nom):
        super().__init__(date_anniv, nom)

    def age_humain(self):
        age = self.calculer_age()
        if age == 0:
            return "Trop jeune pour qu'on puisse estimer son âge"
        if age == 1:
            return self.AGE_1AN
        elif age == 2:
            return self.AGE_2AN
        else:
            return self.AGE_2AN + (self.AJOUT_AGE_APRES_2AN * (age - self.AGE_APRES_LEQUEL_ON_AJOUTE))

    def __str__(self):
        return super().__str__("chat")
