def check_frequency(numbers, target_number):
    frequency = numbers.count(target_number)
    return frequency

my_list = [1, 2, 3, 4, 1, 2, 1, 3, 4, 5, 1]
find = 1
count = check_frequency(my_list, find)
print(f"The frequency of {find} in the list is: {count}")