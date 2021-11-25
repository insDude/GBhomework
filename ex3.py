seasons_of_year = ['зима', 'весна', 'лето', 'осень']
while True:
    try:
        months = int(input('Введите число из диапазона 1-12: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if months in range(1, 13):
        break
    print('Введено число не из диапазона 1-12!')
if months in range (9, 12):
    print(seasons_of_year[3])
elif months in range (6, 9):
    print(seasons_of_year[2])
elif months in range (3, 6):
    print(seasons_of_year[1])
else:
    print(seasons_of_year[0])
