# Recursive product function


def product(int_lst: list) -> int:
    """Multiplies every element of the list as long as they are integers
    args:
        int_list (lst): list of integers.
    returns:
        product (int): the product of the list.
    """
    # Base cases.
    if len(int_lst) == 0:
        return 1
    if len(int_lst) == 1:
        return int_lst[0]
    # Recursive case.
    else:
        head = int_lst[0]
        tail = int_lst[1:]
        return head * product(tail)


if __name__ == "__main__":
    random_list_0 = [2, 3, 5, 12, 4, 9]
    random_list_1 = []
    print(product(random_list_0))
    print(product(random_list_1))
