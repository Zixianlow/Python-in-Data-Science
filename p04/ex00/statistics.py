def ft_median(numbers: list) -> int:
    """return median of list pased"""
    if (len(numbers) == 1):
        return numbers[0]
    elif (len(numbers) % 2):
        return numbers[len(numbers) // 2]
    else:
        return numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1] / 2


def ft_quartile(numbers: list, total) -> None:
    """prints [Q1, Q3] quartile of list pased"""
    print("quartile : [", end="")
    if (len(numbers) == 1):
        print(f'{float(numbers[0])}, {float(numbers[0])}]')
        return
    if len(numbers) == 2:
        print(f'{float(numbers[0])}, {float(numbers[1])}]')
        return
    i = len(numbers) // 2
    if (len(numbers) % 2):
        print(f'{float(ft_median(numbers[:i + 1]))}\
, {float(ft_median(numbers[i:]))}]')
    else:
        print(f'{float(ft_median(numbers[:i]))}\
, {float(ft_median(numbers[i:]))}]')


def ft_statistics(*args: int, **kwargs: str) -> None:
    """prints statistical operation of argument passed"""
    numbers = []
    for i in args:
        try:
            assert isinstance(i, int), "item passed is not an int"
            numbers.append(i)
        except AssertionError as e:
            print(f"AssertionError : {e}")
            return
    total = sum(numbers)
    numbers.sort()
    if (len(numbers) != 0):
        mean = total / len(numbers)
        var = sum([((x - mean) ** 2) for x in numbers]) / len(numbers)
        std = var ** 0.5
    operation = ["mean", "median", "quartile", "std", "var"]
    for i in kwargs:
        if (kwargs[i] in operation and len(numbers) == 0):
            print("ERROR")
            continue
        if (kwargs[i] == "mean"):
            print(f"mean : {mean}")
        elif (kwargs[i] == "median"):
            print(f"median : {ft_median(numbers)}")
        elif (kwargs[i] == "quartile"):
            ft_quartile(numbers, total)
        elif (kwargs[i] == "std"):
            print(f"std : {std}")
        elif (kwargs[i] == "var"):
            print(f"var : {var}")
