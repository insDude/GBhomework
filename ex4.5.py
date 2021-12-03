from functools import reduce

def list(num_1, num_2):
    return num_1 * num_2

new_list = [num for num in range(100, 1001, 2)]
print(f"Исходный список\n{new_list}\nНовый список\n{reduce(list, new_list)}")

