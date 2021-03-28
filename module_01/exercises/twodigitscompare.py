# Porównywanie dwóch wartośći

number1 = int(input('Podaj liczbe 1: '))
number2 = int(input('Podaj liczbe 2: '))

if number1 == number2:
    print(f'Liczby {number1} i {number2} są Sobie równe.')
elif number1 < number2:
    print(f'Liczba {number1} jest mniejsza od {number2}')
elif number1 > number2:
    print(f'Liczba {number1} jest większa od {number2}')
else:
    print('Nie rozumiem')
