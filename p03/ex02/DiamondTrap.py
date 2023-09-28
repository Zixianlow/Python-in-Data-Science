from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King."""
    def __init__(self, name: str, is_alive=True) -> None:
        """King class constructor doc"""
        super().__init__(name, is_alive)

    def __repr__(self):
        """King class __repr__"""
        return f"of Vector: \
    ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __str__(self):
        """King class __str__"""
        return f"of Vector: \
    ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def set_eyes(self, eyes):
        self.eyes = eyes

    def get_eyes(self):
        return self.eyes

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_hairs(self):
        return self.hairs
