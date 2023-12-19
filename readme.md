"Ce projet propose une hiérarchie de classes en Python pour représenter des animaux, des chats et des chiens, avec des méthodes permettant de calculer leur âge humain en fonction de règles spécifiques.

1. **Classe Animal:**
   - Méthode `calculer_age(date_naissance)`: Prend la date de naissance de l'animal, la compare à la date actuelle et retourne l'âge en années.

2. **Classe Chat (héritant de Animal):**
   - Méthode `age_humain()`: Utilise la méthode `calculer_age` de la classe de base pour obtenir l'âge en années, puis applique une logique spécifique pour calculer l'âge en années humaines pour un chat. Si l'âge est 1, l'âge humain est 15 ; s'il est 2, c'est 24. Sinon, ajoute 4 années humaines pour chaque année supplémentaire au-delà de 2.

3. **Classe Chien (héritant de Animal):**
   - Méthode `age_humain()`: Utilise la méthode `calculer_age` de la classe de base pour obtenir l'âge en années, puis applique une logique spécifique pour calculer l'âge en années humaines pour un chien. Si l'âge est 1, l'âge humain est 15 ; s'il est 2, c'est 24. Sinon, ajoute 5 années humaines pour chaque année supplémentaire au-delà de 2.

Ces classes fournissent une structure flexible pour représenter des animaux, des chats et des chiens, tout en permettant de calculer leur âge en années humaines conformément aux règles spécifiées."