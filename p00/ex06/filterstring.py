import ft_filter
import sys


def main():
    """main()

Check the arguments passed via sys.argv and check for symbols or special
character in the argument, then splits the argument into a list. Calls the
ft_filter and print out the filtered result"""
    try:
        assert len(sys.argv) == 3, " the arguments are bad"
        arg = sys.argv[1]
        arg2 = sys.argv[2]
        charset = str(arg)
        for char in charset:
            if char.isprintable():
                assert char.isalnum() or char.isspace(), \
                    " the arguments are bad"
        res = []
        words = charset.split()
        for word in words:
            res.extend([word])
        length = int(arg2)
        print(list(ft_filter.ft_filter(lambda x: len(x) > length, res)))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
