def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Checks the list size of height and weight pass to be same size,
and check for all items in the two list to be having a int or float type.
Then, from the respective list item calculate the bmi, extend it in a
new list and return the result."""
    try:
        assert len(height) == len(weight), " list size not same"
        for item in height:
            assert isinstance(item, int) or isinstance(item, float), \
                " height item is not int or float"
        for item in weight:
            assert isinstance(item, int) or isinstance(item, float), \
                " weight item is not int or float"
        i = 0
        res = []
        for item in height:
            res.extend([weight[i]/item/item])
            i += 1
        return res
    except AssertionError as e:
        print(f"AssertionError: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    for item in bmi:
        if (item > limit):
            res.extend([True])
        else:
            res.extend([False])
    return res
