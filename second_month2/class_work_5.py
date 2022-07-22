#регрулярныйе выражения
# import re


"""
geektech@gmail.com
title = geektech
@
damin_name = gmail
.
domin = com
"""

# import re
#
# email ='geektech@gamil.com'
# is_valid = re.search(r'.+[a-zA-Z0-9]@(gmail|yandex|mail)\.(com|ru)',email)
#
# try:
#     if email[is_valid,stat():is_valid.end()] ==email:
#         print('is vallid email')
#     expend:
#         print('is invalid email')







"""

phone_number = +996 -777-77-77-77
+
ISO_code = 996
-
operator_code = 777
-
77
-
77
-
77
-
77

"""

import re

phone = "+996-777-77-77-77"
is_valid = re.search(r"\+996-([0-9]{3})-([0-9]{2})-([0-9]{2})-([0-9]{2})", phone)

print(is_valid)

try:
    if phone [is_valid.start():is_valid.end()] ==phone:
        print('Is Valid Phone Numeber')
except:
    print("Is Invalid Phone Number")