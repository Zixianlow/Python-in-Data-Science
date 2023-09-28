import sys


def main():
    """main()

Check the arguments passed via sys.argv and ask for user input if argument
count is only one. Next, calculate upper, lower, space, digit, punctuation
in the line, then print out the result"""
    upper = 0
    lower = 0
    punc = 0
    space = 0
    digit = 0
    total = 0

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            print("What is the text to count?")
            arg = sys.stdin.readline()
        else:
            arg = sys.argv[1]
        for char in arg:
            total += 1
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isspace():
                space += 1
            elif char.isdigit():
                digit += 1
            elif char.isprintable():
                punc += 1
        print("The text contains", total, "characters:")
        print(upper, "upper letters")
        print(lower, "lower letters")
        print(punc, "punctuation mark")
        print(space, "spaces")
        print(digit, "digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
