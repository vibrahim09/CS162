# Recursive function to find balance parenthesis.


def balance(string: str) -> bool:
    if string.startswith("(") and string.endswith(")"):
        return "Balance parenthesis"


if __name__ == "__main__":
    string = "()"
    print(balance(string))
