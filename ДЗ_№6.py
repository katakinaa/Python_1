data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
deleted = numbers.pop(numbers.index(True))
letters.append(deleted)
numbers.insert(numbers.index(3) + 1, 2)

numbers.sort()
letters.reverse()
letters[letters.index('C')] = 'c'
letters[letters.index('g')] = 'G'

numbers = [num ** 2 for num in numbers]

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)

print(letters_tuple)
print(numbers_tuple)
