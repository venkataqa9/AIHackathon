def filter_duplicates(arr):
    return list(set(arr))

# Example usage
my_array = ["apple", "banana", "apple", "orange", "banana"]
filtered_array = filter_duplicates(my_array)
print(filtered_array)