# First Option
my_list = ["apple", "banana", "cherry", "apple", "orange", "banana"]

unique_list = []
for x in my_list:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)

# Second Option
my_list = ["apple", "banana", "cherry", "apple", "orange", "banana"]

unique_list = list(set(my_list))

print(unique_list)
