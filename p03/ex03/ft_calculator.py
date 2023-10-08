class calculator:
    """calculator class"""
    def __init__(self, list):
        """calculator class constructor doc"""
        self.list = list

    def __add__(self, object) -> None:
        """calculator add operation doc"""
        res = []
        for item in self.list:
            res.append(item + object)
        self.list = res
        print(res)

    def __mul__(self, object) -> None:
        """calculator multiply operation doc"""
        res = []
        for item in self.list:
            res.append(item * object)
        self.list = res
        print(res)

    def __sub__(self, object) -> None:
        """calculator subtract operation doc"""
        res = []
        for item in self.list:
            res.append(item - object)
        self.list = res
        print(res)

    def __truediv__(self, object) -> None:
        """calculator division operation doc"""
        try:
            res = []
            for item in self.list:
                res.append(item / object)
            self.list = res
            print(res)
        except ZeroDivisionError:
            print("ZeroDivisionError: float division by zero")
