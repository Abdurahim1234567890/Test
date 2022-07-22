# from PERSON.create_person import create
# #from  PERSON import create_person
#
# jack = create('jaclk', 'barbaro', 20)
# print(jack.get_full_name())



#дз 6

# import random
# from typing import Union, List
#
#
# class Arrays:
#     def __init__(self):
#         self.nesting = random.randint(50, 150)
#         self.arrays = self.get_array(1)
#
#     def get_array(self, step) -> Union[List[list], int]:
#         if step <= self.nesting:
#             return [self.get_array(step + 1)]
#         else:
#             return random.randint(1_000, 100_000)
#
#
# nested_arrays = Arrays()
#
# class Solution:
#
#     def get_num(self, arrays: list) -> int:
#         if isinstance(arrays[0], int):
#             print(arrays[0])
#             return
#         return self.get_num(arrays[0])
#
# Solution().get_num(nested_arrays.arrays)











# Дз 5

# import re
#
# class ValidCarNumber:
#     def __init__(self, number):
#         self.number = number
#
#     def is_valid(self):
#         iss = re.search("0([0-9]{1})KG([0-9]{3}[A-Z]{3})", self.number)
#         try:
#             if iss.end() == len(self.number):
#                 return "Valid Car Number"
#             else:
#                 raise ValueError
#         except:
#            return "Invalid Car Number"
#
#
# car_number = input("Введите номер машины: ")
# num = ValidCarNumber(car_number)
#
# print(num.is_valid())





























# def say_hello(username):
#     print(f' {username}, hello!')
#
#
# sekret_key ='12412515235266'









































# Дз2
# class Human:
#    defalt_name = None
#    defalt_age = 0
#
#    def __init__(self, name=defalt_name, age=defalt_age):
#
#        self.name = name
#        self.age = age
#        self._money = 0
#        self._home = None
#
#    def info(self):
#         print(f'name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self._money}')
#         print(f'Home: {self._home}')
#
#    def defalt_info():
#             print(f' Defalt_Name: {self.defalt_name}')
#             print(f' Defalt_Age: {self.defalt_age}')
#
#    def earn_money(self, amount):
#         self.money += amount
#         print(f'Earn {amount} money!  Current value:{self._money}')
#
#    def buy_home(self, home, discont):
#        price =home.final_price(discont)
#        if self._money >=price:
#            self._make_deal(home,price)
#        else:
#            print('Not_many')
#
# class Home:
#     def __init__(self, _area, _price):
#         self._area = _area
#         self._price = _price
#
#     def final_price(self, discont):
#         self.discont = discont
#         final.price = self._price * (100 - discont) / 100
#         print(f' Final_price : {final_price}')
#         return final_price
#
# class SmallHome(Home):
#     def __init__(self, price, _area):
#         super().__init__(_area, price)
#
# Abdurahim = Human (' Abu', 17)
# Abdurahim.info()
#
# small_home = SmallHome (8_500, 500)
# Abdurahim.buy_home(SmallHome, 5)
# Abdurahim
# Abdurahim.earn_money(5_000)
# Abdurahim.buy_home(SmallHome, 5)
# Abdurahim.earn_money(5000000000)
# Abdurahim = Home (Two-StoryHome)
# Abdurahim.info()



#дз 3
#
# class Fracton:
#     def __init__(self, numerator, denumerator):
#         self.numerator = numerator
#         self.denumerator = denumerator
#
#     def GCD (self, a, b):
#         return (self.GCD(b, a % a) if a else b)
#
#
#     def __add__(self, other):
#         znam = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
#         cisl = znam // self.numerator * other.numerator +\
#                znam // other.denumerator * other.numerator
#         self.denumerator = cisl
#         self.numerator = znam
#         return Fracton (numerator=znam, denumerator=cisl)
#
#     def __sub__(self, other):
#         znam = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
#         cisl = znam // self.numerator * other.numerator - \
#                znam // other.denumerator * other.numerator
#         self.denumerator = cisl
#         self.numerator = znam
#         return Fracton (numerator=self.numerator, denumerator=self.denumerator)
#
#     def __mul__(self, other):
#         znam = self.denumerator * other.denumerator
#         cisl = self.numerator * other.numerator
#         k = self.GCD(self, other)
#         znam // k
#         cisl // k
#         self.numerator = cisl
#         self.denumerator =znam
#         return Fracton(numerator=self.numerator, denumerator=self.denumerator)
#
#     def __floordiv__(self, other):
#         n = other.numerator
#         other.numerator = other.denumerator
#         other.denumerator = n
#         znam = self.numerator * other.numerator
#         cisl = self.denumerator * other.denumerator
#         k = self.GCD(self, other)
#         znam // k
#         cisl // k
#         self.numerator = cisl
#         self.denumerator = znam
#         return Fracton(numerator=self.numerator, denumerator=self.denumerator)
#
#     def __str__(self):
#         return f'{self.numerator} / {self.denumerator}'
#
# num1 = input("Введите дробь в формате ?/?: ").split('/')
# num2 = input("Введите дробь в формате ?/?: ").split('/')
#
# a = Fraction(int(num1[0]), int(num1[1]))
# b = Fraction(int(num2[0]), int(num2[1]))
#
# print(f"{num1[0]}/{num1[1]} + {num2[0]}/{num2[1]} = {a + b}")
# a = Fraction(int(drob1[0]), int(drob1[1]))
# print(f"{num1[0]}/{num1[1]} - {num2[0]}/{num2[1]} = {a - b}")
# a = Fraction(int(num1[0]), int(num1[1]))
# print(f"{num1[0]}/{num1[1]} * {num2[0]}/{num2[1]} = {a * b}")
# a = Fraction(int(num1[0]), int(num1[1]))
# print(f"{num1[0]}/{num1[1]} // {num2[0]}/{num2[1]} ={a // b}")






















# import  re
#
# class ValidCarNumber:
#     def __init__(self,number):
#         self.number = number
#
#     def is_valid (self):
#         iss = re.search("0 [0-9]{1}KG([0-9]){3}([A-Z] {2-3})", self.number)
#         try:
#             if iss.end() ==len(self.number):
#                 return  "Номер не валидный!"
#         except:
#             return  "Номер валидный!"
#
# car_number = input('Введите номер машины:' )
# num = ValidCarNumber(car_number)
#
# print(num.is_valid())








#
# import re
# class ValidCarNumber:
#     def __init__(self, number):
#         self.number = number
#     def is_valid(self):
#         is_number = re.search(r'([0-9]{2})([A-Z]{2})([0-9]{3})([A-Z]{3})', self.number)
#         try:
#             if self.number[is_number.start():is_number.end()] == self.number:
#                 return f'Is valid number'
#         except:
#             return f'Is invalid number'
#
# number = input("Ввкеди номер машины: ")
# Mers = ValidCarNumber('07KG567BAD')
# print(Mers.is_valid())



















