# 1 Написать функцию, которая возвращает первое слово из полученного предложения.

sentence = input('Ваше предложение: ')
def first_word(sentence='Hello world'):
    return sentence.split()[0]
if sentence == '':
    print(first_word())
else:
    print(first_word(sentence))

# 2 Написать функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое.

nums = []
while True:
    numbers = int(input('Введите число: '))
    def average(*args):
        nums.append(numbers)
        print(nums, 'nums')
        args = sum(nums) // len(nums)
        return args
    print(average(nums))


#3 Написать функцию, проверяющую надежность пароля.

while True:
    password = input('your password: ')
    def validity(obj):
        if len(password) >= 6:
            if password.isalpha():
                print('Используйте цифры тоже !')
            elif password.isdigit():
                print('Используйте буквы тоже !')
            else:
                return obj, 'Надёжный пароль !'
        else:
            return False
    print(validity(password))

