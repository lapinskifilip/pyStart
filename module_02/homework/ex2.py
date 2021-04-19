option = input('Co chcesz zamienic? \n 1. Dwojkowa \n 2. Dziesietna \n Wybor: ')

if option == '1':
    value = input('Podaj wartosc w systemie dwojkowym: ')
    result = 0
    for index, number in enumerate(value):
        result += int(number) * 2 ** (len(value) - index - 1)
    print(f'Wartosc w systemie binarnym to: {result}')
elif option == '2':
    value = int(input('Podaj wartosc w syustemie dwojkowym: '))
    print(f'Wartosc w systemie binarnym to: {value:b}')
else:
    print('Nie rozumiem')