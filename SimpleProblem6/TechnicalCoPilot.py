def find_largest_integer(lst):
    largest_integer = None
    for sublist in lst:
        for item in sublist:
            if isinstance(item, int):
                if largest_integer is None or item > largest_integer:
                    largest_integer = item
    return largest_integer

