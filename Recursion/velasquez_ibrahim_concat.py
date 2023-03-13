# String concat using recursion


def concat(string_list: list) -> str:
    """Concatenates a list of strings using recursion.
    args:
        string_list (list): list of strings.
    returns:
        string (str): string that represents the concatenated string_list.
    """
    if len(string_list) == 1:
        return string_list[0]
    if len(string_list) == 0:
        return "List is empty."
    else:
        head = string_list[0]
        tail = string_list[1:]
        return head + concat(tail)


if __name__ == "__main__":
    random_list_0 = ["Ibrahim", "Velasquez", "is", "30", "years", "old"]
    random_list_1 = []
    print(concat(random_list_0))
    print(concat(random_list_1))
