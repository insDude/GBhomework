def sum():
    amount = 0
    while True:
        list = input('Введите числа через пробелм или Q для выхода из программы: ').split()
        for num in list:
            if num == 'q':
                return amount
            else:
                try:
                    amount += int(num)
                except ValueError:
                    print('Для выхода из программы нажмите Q: ')
        print(f'Сумма чисел = {amount}')
print(sum())
