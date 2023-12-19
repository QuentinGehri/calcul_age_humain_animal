from Animal import Animal


class Chat(Animal):
    def __init__(self, date_anniv, nom):
        super().__init__(date_anniv, nom)

    def age_humain(self):
        pass

    def __str__(self):
        return super().__str__("chat")
    