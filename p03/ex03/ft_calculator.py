class calculator:
    """calculator class"""
    def __init__(self, list):
        """calculator class constructor doc"""
        self.list = list

    def __add__(self, object) -> None:
        """calculator add operation doc"""
        for item in self.list:
            item += object
        print(self.list)

    def __mul__(self, object) -> None:
        """calculator multiply operation doc"""
        for item in self.list:
            item *= object
        print(self.list)

    def __sub__(self, object) -> None:
        """calculator subtract operation doc"""
        for item in self.list:
            item -= object
        print(self.list)

    def __truediv__(self, object) -> None:
        """calculator division operation doc"""
        try:
            for item in self.list:
                item /= object
            print(self.list)
        except ZeroDivisionError:
            print("ZeroDivisionError: float division by zero")
