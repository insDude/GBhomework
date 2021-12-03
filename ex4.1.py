from sys import argv

def money():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"money - {time * rate + bonus}")
    except ValueError:
        print("Нужно ввести три числа.")
money()
