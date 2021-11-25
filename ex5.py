rating = [7, 6, 4, 2, 2, 2, 5, 5, 6, 7, 15, 8]
while True:
    try:
        element = int(input('Введите натуральное число: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if element > 0:
        rating.append(element)
        rating.sort(reverse=True)
        break
    print('Это ненатуральное число!')
print(rating)