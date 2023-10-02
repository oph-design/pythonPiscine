import sys
from ft_filter import ft_filter

def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isnumeric(), "the arguments are bad"
    except AssertionError as msg:
        print(msg)
        exit(1)
    print(ft_filter(sys.argv[1], int(sys.argv[2])))

main()
