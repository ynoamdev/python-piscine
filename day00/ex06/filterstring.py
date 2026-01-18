from ft_filter import ft_filter
import sys


def error():
    """
        func: error()
    """
    print("AssertionError: the arguments are bad")


def main():
    """
        func: main()
    """
    args = sys.argv[1:3]
    if len(args) > 2 or len(args) == 0:
        error()
        return 1
    try:
        x = int(args[1])
    except:
        error()
        return 1
    words = args[0].split()
    result = ft_filter(lambda w: len(w) >= x, words)
    print([i for i in result])


if __name__ == "__main__":
    main()
