from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init(self,name: str,):
        super().__init__(name, self.GRAMS, self.PRICE, self.CALORIES)
