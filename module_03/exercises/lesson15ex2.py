done = False

value = int(input('Podaj liczbe: '))
values = [value]
while not done:
    value2 = int(input('Podaj nowa liczbe: '))
    if value2 < value:
        done = True
    else:
        values.append(value2)
        value = value2

print(values)
print('Srednia', sum(values) / len(values))
