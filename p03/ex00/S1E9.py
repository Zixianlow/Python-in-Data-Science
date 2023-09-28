from abc import ABC, abstractmethod


class Character(ABC):
    """Character class defination inheirited from ABC"""
    def __init__(self, name: str, is_alive=True) -> None:
        self.first_name = name
        self.is_alive = is_alive
        super().__init__()

    @abstractmethod
    def die(self):
        """Character abstract method doc"""
        pass


class Stark(Character):
    """Stark Class, inheirited from Character doc"""
    def __init__(self, name: str, is_alive=True) -> None:
        """Stark class constructor doc"""
        super().__init__(name, is_alive)

    def die(self):
        """Stark abstract method doc"""
        self.is_alive = False
