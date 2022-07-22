data_tuple = ['h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g']
letters = []
numbers = []

for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
 if type(data_tuple[i]) == str:
     letters.append(data_tuple[i])
 elif type(data_tuple[i]) == bool:
     letters.append(data_tuple[i])
 elif type(data_tuple[i]) == int:
     numbers.append(data_tuple[i])
 elif type(data_tuple[i]) == float:
     numbers.append((data_tuple[i]))

letters.insert(9, True)
letters.remove(letters[9])
letters[7] = 'G'
letters[1] = 'c'

letters = letters[::-1]
letters_tuple = tuple(letters)
print(letters_tuple)

numbers.remove(numbers[0])
numbers.insert(1, 2)

for i in (0, 1, 2):
    numbers[i] = numbers[i]**2

numbers = numbers[::-1]
numbers_tuple = tuple(numbers)
print(numbers_tuple)