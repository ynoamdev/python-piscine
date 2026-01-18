import sys

UPPER_LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_LETTER = "abcdefghijklmnopqrstuvwxyz"
DIGIT_LETTER = "0123456789"


def calc(s: str) -> dict:
    """func: calc(s: str)-> dict
       return {
        "upper": .,
        "lower": .,
        "space": .,
        "digit": .,
        "mark" : .
       }
    """

    text = {
        "upper": 0,
        "lower": 0,
        "space": 0,
        "digit": 0,
        "mark": 0
    }
    for c in s:
        if c in UPPER_LETTER:
            text["upper"] += 1
        elif c in LOWER_LETTER:
            text["lower"] += 1
        elif c in DIGIT_LETTER:
            text["digit"] += 1
        elif c == ' ' or c == '\n':
            text["space"] += 1
        else:
            text["mark"] += 1
    return text


def print_result(result: dict):
    """func: print_result"""
    upper, lower, space, digit, mark = result.values()
    sum_letters = upper + lower + digit + space + mark
    print(f"The text contains {sum_letters} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{mark} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def argc() -> int:
    """func: argc"""

    argc = 0
    for c in sys.argv:
        argc += 1
    return argc


def main():
    """func: main"""

    if argc() > 2:
        print("AssertionError: Too many args")
    elif argc() == 2:
        r = calc(sys.argv[1])
        print_result(r)
    else:
        print("What is the text to count?")
        text = sys.stdin.readlines()
        r = calc("".join(text))
        print_result(r)


if __name__ == "__main__":
    main()
