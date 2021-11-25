add_str = input('Введите значения через запятую: ')
add_list = add_str.split(',')
print(add_list)
index = 1
while index < len(add_list):
    add_list[index], add_list[index-1] = add_list[index-1], add_list[index]
    index +=2
