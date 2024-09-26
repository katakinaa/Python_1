def nearest_number(numbers, int_num):
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - int_num))
    return (int_num, sorted_numbers)


result1 = nearest_number([312, 996, 31, 1991], 1000)
print(result1)

result2 = nearest_number([5, 20.18, 103, 4], 27)
print(result2)


# примеры использования lambda функций с такими функциями как filter, map

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_numbers = list(filter(lambda x: x % 3 == 0, numbers))
print(filter_numbers)

numbers = [1, 2, 3]
map_numbers = list(map(lambda x: x**3, numbers))
print(map_numbers)
