eng = 'qwertyuiopasdfghjkzxcvbnm'
rus = 'цукенгшщзхъйфывапролджэячсмитьбю'
enggl = 'eioay'
rusgl = ' ауоыэяюёие'
while True:
    word = (input('\nВведите любое Слово:\n')).lower()
    if word == 'exit':
        break
    gl = 0
    sogl = 0
    for i in word:
        if i in eng:
            if i in enggl:
                gl+=1
            else:sogl+=1
        elif i in rus:
            if i in rusgl:
                gl+=1
            else:sogl+=1
    kol = len(word)
    print(f'Слово : {word}')
    print(f'Количество букв: {len(word)}')
    print(f'Согласные буквы: {sogl}')
    print(f'Гласные буквы: {gl}')
    print(f'Гласные/Согласные: {round(gl/kol*100 , 2)}% / {round(sogl/kol*100, 2)}%')


