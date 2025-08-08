from task_11 import Dessert


class JellyBean(Dessert):
    flavor = None

    def set_flavor(self, flavor):
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        super().is_delicious()
