list = [5, 7, 10, 15, 4, 16, 33, 3, 25]
larger_num = [list[num] for num in range (0, len(list)) if list[num] > list[num - 1]]
print(larger_num)
