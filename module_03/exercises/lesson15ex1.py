numbers = []
count = 1
while len(numbers) < 10:
    numbers_input = int(input(f'Potrzebujemy 10 dodatnich liczb, podaj {count} z nich: '))
    if numbers_input <= 0:
        print(f'Liczba {numbers_input} nie jest dodatnia')
    else:
        numbers.append(numbers_input)
        count += 1

print(numbers)