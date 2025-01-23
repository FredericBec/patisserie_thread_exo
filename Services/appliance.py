class Appliance:
    def __int__(self, ingredients=None):
        self.ingredients = ingredients if ingredients else []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Ingredient ajouté: {ingredient}")

    def display_ingredients(self):
        print("Ingrédients dans l'appareil")
        print("- ".join(ingredient for ingredient in self.ingredients))

    def bake(self):
        print("Préparation d'un appareil à gâteau :")
        print("Mélanger les ingrédients jusqu'à obtenir une texture homogène.")
        self.display_ingredients()
