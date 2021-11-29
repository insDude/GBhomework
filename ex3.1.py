def div(a, b):
    try:
        a, b = int(a), int(b)
        div_num = a / b
    except ValueError:
        return 'Некорректное число'
    except ZeroDivisionError:
        return 'Деление на ноль запрещено'
    return round(div_num, 2)
print(div(input('Введите число: '), input('Введите второе число: ')))
