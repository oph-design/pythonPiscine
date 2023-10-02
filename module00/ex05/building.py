import sys


def main():
    try:
        assert len(sys.argv) < 3, "too many arguments provided"
    except AssertionError as msg:
        print(msg)
        exit(1)
    if (len(sys.argv) < 2):
        str = input("What is the text to count?\n")
    else:
        str = sys.argv[1]
    print(f"The text contains {len(str)} characters:")
    print(f"{sum(1 for c in str if c.isupper())} upper letters")
    print(f"{sum(1 for c in str if c.islower())} lower letters")
    pnum = sum(1 for c in str if c in ('!', ',' ,';' , '.', '-' ,'?'))
    print(f"{pnum} punctuation marks")
    print(f"{sum(1 for c in str if c == ' ')} digits")
    print(f"{sum(1 for c in str if c.isnumeric())} digits")


main()
