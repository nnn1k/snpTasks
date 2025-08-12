class Dessert:

    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def set_name(self, name):
        self.name = name

    def set_calories(self, calories):
        self.calories = calories

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def is_healthy(self):
        if not isinstance(self.calories, (int, float)):
            return False
        return self.calories < 200

    def is_delicious(self):
        return True
