# Recursive function to find balance parenthesis.


def balance(string: str) -> bool:
    if string.startswith("(") and string.endswith(")"):
        return "Balance parenthesis"
    return False


if __name__ == "__main__":
    string = "()()("
    print(balance(string))
