numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

count_of_numbers = len(numbers)

numbers_without_none = numbers[:4] + numbers[5:]
sum_of_numbers = sum(numbers_without_none)

none_number = sum_of_numbers / count_of_numbers

correct_numbers = numbers
correct_numbers[4] = none_number

print("Измененный список:", correct_numbers)
