def pers_information(**kwargs):
    return ' '.join(kwargs.values())

name = input('Введите name: ')
surname = input('Введите surname: ')
birthday = input('Введите birthday: ')
city = input('Введите city: ')
email = input('Введите email: ')
phone = input('Введите phone: ')
car = input('Введите car: ')

print(pers_information(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone, car=car))

