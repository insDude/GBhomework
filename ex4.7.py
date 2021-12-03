def gen(number):
    num = 1
    if number == 0:
        yield f'{number}! = 1'
    for el in range(1, number + 1):
        num *= el
        yield f'{el}! = {num}'

for i in gen(int(input('Факториал: '))):
    print(i)

