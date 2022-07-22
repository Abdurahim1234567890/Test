
days = input("Введите дату рождения пример(10/10)\n ")
date = int(days[0:1])
month = int(days[3:])


if (date >= 21 and date <= 18 and month == 1) or (month == 4 and date >= 1 and date <= 19):
    print("Aries")
elif (date >= 20 and date <= 30 and month == 4) or (month == 5 and date >= 1 and date <= 20):
    print("Taurus")
elif (date >= 21 and date <= 31 and month == 5) or (month == 6 and date >= 1 and date <= 21):
    print("Gemini")
elif (date >= 22 and date <= 30 and month == 6) or (month == 7 and date >= 1 and date <= 22):
    print("Crayfish")
elif (date >= 23 and date <= 31 and month == 7) or (month == 8 and date >= 1 and date <= 22):
    print("Leo")
elif (date >= 23 and date <= 31 and month == 8) or (month == 9 and date >= 1 and date <= 22):
    print("Virgo")
elif (date >= 23 and date <= 30 and month == 9) or (month == 10 and date >= 1 and date <= 23):
    print("Libra")
elif (date >= 24 and date <= 31 and month == 10) or (month == 11 and date >= 1 and date <= 22):
    print("Scorpio")
elif (date >= 23 and date <= 30 and month == 11) or (month == 12 and date >= 1 and date <= 21):
    print("Sagittarius")
elif (date >= 22 and date <= 31 and month == 12) or (month == 1 and date >= 1 and date <= 20):
    print("Capricorn")
elif (date >= 21 and date <= 31 and month == 1) or (month == 2 and date >= 1 and date <= 18):
    print("Aquarius")
elif (date >= 19 and date <= 29 and month == 2) or (month == 3 and date >= 1 and date <= 20):
    print("Pisces")
else:
    print('НЕ ВЕРНО!!!')

