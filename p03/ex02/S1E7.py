from S1E9 import Character
import collections


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name: str, is_alive=True) -> None:
        """Baratheon class constructor doc"""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        """Baratheon class __repr__"""
        return f"of Vector: \
    ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __str__(self):
        """Baratheon class __str__"""
        return f"of Vector: \
    ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def die(self):
        """Baratheon abstract method doc"""
        self.is_alive = False


class Lannister(Character):
    models = collections.defaultdict(list)

    def __init__(self, name: str, is_alive=True) -> None:
        """Lannister class constructor doc"""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        """Baratheon class __repr__"""
        return f"of Vector: \
('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """Baratheon class __str__"""
        return f"of Vector: \
('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Lannister abstract method doc"""
        self.is_alive = False

    def create_lannister(self, name: str, is_alive=True):
        """Lannister creates Lannister"""
        cls = Lannister(name, is_alive)
        return cls
