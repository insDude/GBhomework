with open('3.txt', 'r', encoding='utf-8') as f:
    people = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'salary = {round(sum(people.values()) / len(people), 3)}\n'
          f'Сотрудники с зп ниже 20.000 {[e[0] for e in people.items() if e[1] < 20000]}')
