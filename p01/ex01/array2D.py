import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Checks the family passed is a list and checks the content in the
list to have the same size accross. Then, print out the initial shape and
slice based on the start end position and print out the new shape. Finally,
return the resultant list"""
    try:
        assert isinstance(family, list), " family is not a list"
        i = 0
        j = len(family[0])
        for item in family:
            assert len(item) == j, " list size not same"
            i += 1
        res = np.array(family)
        print("My shape is :", res.shape)
        res = res[start:end]
        print("My new shape is :", res.shape)
        return res.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
