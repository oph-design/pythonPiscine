import sys


try:
    assert len(sys.argv) == 2, "more than one arguments provided"
    assert sys.argv[1].isnumeric() == 1, "argument is not an integer"
except AssertionError as msg:
    print(msg)
    exit(1)

if (int(sys.argv[1]) % 2 == 0):
    print("I\'m Even")
else:
    print("I\'m Odd")
