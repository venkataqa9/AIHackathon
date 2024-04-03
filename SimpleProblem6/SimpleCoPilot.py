def find_largest_integer(list_of_lists):
    max_number = float('-inf')  # Initialize with negative infinity

    for sublist in list_of_lists:
        for number in sublist:
            if number > max_number:
                max_number = number

    return max_number