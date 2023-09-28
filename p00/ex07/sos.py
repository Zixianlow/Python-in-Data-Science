import sys


def main():
    """main()

Check the arguments passed via sys.argv and check for symbols or special
character in the argument. Then, print the morse code of the line"""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    try:
        assert len(sys.argv) == 2, " the arguments are bad"
        arg = sys.argv[1]
        arg = arg.upper()
        for char in arg:
            assert char in NESTED_MORSE, " the arguments are bad"
        for char in arg:
            print(NESTED_MORSE[char], end="")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
