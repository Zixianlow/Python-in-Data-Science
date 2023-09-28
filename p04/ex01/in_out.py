def square(x: int | float) -> int | float:
    """return x ^ 2"""
    return x * x


def pow(x: int | float) -> int | float:
    """return x ^ x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer function returns an object with inner function"""
    count = 0

    def inner() -> float:
        """return based on function passed by iteration of count"""
        nonlocal count
        count += 1
        if (count == 1):
            res = function(x)
        else:
            i = 0
            res = x
            while i < count:
                res = function(res)
                i += 1
        return res
    try:
        assert isinstance(x, int) or isinstance(x, float), \
            "x is not a int or float."
        return inner
    except AssertionError as e:
        print(f"AssertionError: {e}")
