dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('4a.txt', 'w', encoding='utf-8') as af:
    with open('4b.txt', 'r', encoding='utf-8') as bf:
#       af.write(str([line.replace(line.split()[0], dict.get(line.split()[0])) for line in bf]))

