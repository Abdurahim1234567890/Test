"""

DATA Structur


"""


#list=[1, 2, 3, 4, 5]

"""

list, set, tuple


"""



"""

Linked List-
What is?

"""







#------------------------------------------------------------------------------------------------------------------------




"""
Hach Table

"""


#
# user_age = {"ali:17"
#             "eren:17"
#             "almaz:17"
#             "azamat:25"
#             "aidegin:17"
#             "bekzat:18"
#             "abdurahim:17"
#             "key": "value"
#             }
#
#
# name = input("Name: ")
# print(user_age[name])
#
#

"""
Big o (1)

"""



#--------------------------------------------------------------------------------------------------------------------






"""

Recursiya

"""


# def rec (step: int):
#     print(step)
#
#     """" Base """
#     if step == 10:
#         return
#
# """Recursion"""
#     rec(step+1)
#
# rec(1)
#


mass = [7, 86756, 4, -8, 1, 2, 43, -86, 28, 57, 3246, 264375, -34534, 4633]

"""
Big o (n * n)

"""

for i in range(len(mass)):
    for j in range(i, len(mass)):
        if mass[i] < mass [j]:
            mass[i], mass[j] = mass[j], mass[i]


print(mass)
