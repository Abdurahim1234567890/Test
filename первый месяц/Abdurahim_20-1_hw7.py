# первое второе третье задание
#после каждой проверки индекса счетчик обнуляеться 
ten = [i for i in range(1, 11)]
print(ten)
evens = list(filter(lambda x: x % 2 == 0 , ten))
print(evens)
kvadrat_stepen = list(map(lambda y:y**2, evens))
print(kvadrat_stepen)
# Четвертое задание

def t(ten):
    while True:
        print(ten)
        menu = input('1)start\n2)exit')
        if menu == '1':
            try:
                index = int(input("Введите индекс!:"))
                index1 = index
                print(ten[index1])

            except Exception:
                print(f'Введиде правельный индекс: {ten}')
                continue
        elif menu == '2':
            break

t(ten)
