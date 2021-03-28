numbers = tuple(range(12,1024,6))

print(f'Liczb podzielny przez 6 z zakresu od 12 do 1024 jest: {len(numbers)}')
print(f'Trzy pierwsze liczby z tego zakresu to: {numbers[:3]}')
print(f'Przedostatni element tego zakresu to: {numbers[-2]}')
print(f'Co szosty element zaczynajac od 4: {numbers[4::6]}')
print(f'Co trzeci element licząc od końca: {numbers[-1:1:-3]}')

print(f'Srednia ostatnich 10 cyfr to: {int(sum(numbers[-10::1]) / 10)}')

