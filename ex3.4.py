def func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'X должен быть больше нуля, Y должен быть меньше нуля!'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
                return f'Результат возведения x в степень y: {round(result, 2)}'
    except ValueError:
        return 'Нужны только числа'
print(func(25, -5))
