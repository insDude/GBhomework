seasons_dict = dict(winter='зима', spring='весна', summer='лето', autumn='осень')
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
    print(seasons_dict.get('autumn'))
elif months in range (6, 9):
    print(seasons_dict.get('summer'))
elif months in range (3, 6):
    print(seasons_dict.get('spring'))
else:
    print(seasons_dict.get('winter'))
