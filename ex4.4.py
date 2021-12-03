from random import randint

list = [randint(-6, 8) for _ in range(18)]
new_list = [num for num in list if list.count(num) == 1]
print(f"Исходный список\n{list}\nНовый список\n{new_list} ")

print(a := [randint(0, 9) for b in range(18)], '\n', [c for c in a if a.count(c) == 1], sep="")

