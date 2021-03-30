from math import sqrt

number = int(input('Podaj prosze liczbe: '))

if number < 2:
    print('Nie jest to liczba pierwsza')
elif number % number == 0:
    print('Jest to liczba pierwsza')