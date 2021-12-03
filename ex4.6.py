from itertools import count, cycle

print("Программа выводит числа, согласно указанного числа. Для начала работы программы необходимо нажать Enter, для выхода q")
for num in count(int(input("Введите число: "))):
    print(num, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы первого списка. Для продолжении работы программы необходимо нажать Enter, для выхода нажмите q.')
list = input('Введите список числе через пробел: ').split()
new_list = cycle(list)
quit = None
while quit != 'q':
    print(next(new_list), end='')
    quit = input()






