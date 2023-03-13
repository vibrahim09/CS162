# Recursive function to find balance parenthesis.


def balance(string: str) -> bool:
    """Returns True if there the parenthesis in the given string are balance
    args:
        string (str): the string to check if it is balanced.

    returns:
        bool: True if parenthesis in string are/is balanced.
    """
    if len(string) == 0:
        return True
    close = string.find(")")
    if close == -1:
        return False
    open = string.rfind("(", 0, close)
    if open == -1:
        return False
    new_string = string[:open] + string[close + 1 :]
    return balance(new_string)


if __name__ == "__main__":
    string = "(((ibrahim)))(19)(!@#$%^&*)"  # balanced
    string2 = "(((ibrahim))))(19)(!@#$%^&*)"  # not balanced
    string3 = "(((ib))))"  # not balanced
    string4 = ")("  # not balanced
    string5 = "(()())"  # balanced

    print(f"{string} is {balance(string)}")
    print(f"{string2} is {balance(string2)}")
    print(f"{string3} is {balance(string3)}")
    print(f"{string4} is {balance(string4)}")
    print(f"{string5} is {balance(string5)}")
