left = 0
right = 100
middle = 50
i = 0
cif = input("Да , < , >: ")
with open('results.txt', 'w', encoding='UTF-8') as file:
 while True:
  print(f"Загаданное вами число равно {middle}?")
  file.write(f"{middle} ")
  otvet = input()
  i += 1
  if otvet == '>':
   left = middle
   middle = (left + right) // 2
  elif otvet == '<':
   right = middle
   middle = (left + right) // 2
  elif otvet.lower() == 'да':
   file.write(f"Попытки: ")
   file.write(f"\nКоличество попыток: {i}")
   file.write(f"\nЗагаданное число: {middle}")
   break
  else:
   print('Нераспознанная операция )')
