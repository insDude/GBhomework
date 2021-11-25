words = input('Введите строку из нескольких слов: ').split()
for index, element in enumerate(words, 1):
    print(f'{index}: {element[:10]}')