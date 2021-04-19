pesel =input('Podaj PESEL: ')
check = '13791379131'

control = 0
for index, _ in enumerate(pesel):
    control += int(pesel[index]) * int(check[index])

if str(control)[-1] == '0':
    print('Pesel jest prawidlowy')
else:
    print('Pesel jest nie prawidlowy')