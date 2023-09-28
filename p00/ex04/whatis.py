import sys

if len(sys.argv) == 1:
    sys.exit(0)
try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    arg = sys.argv[1]
    integer = int(arg)
    if integer % 2 == 1:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print("AssertionError: argument is not an integer")
