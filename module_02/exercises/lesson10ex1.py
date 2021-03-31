numbers = list(range(1,101))

div_by_4 = 0
div_by_4_numbers = []

div_by_5 = 0
div_by_5_numbers = []

for number in numbers:
    if number % 4 == 0:
        div_by_4_numbers.append(number)
        div_by_4 += 1
    if number % 5 == 0:
        div_by_5_numbers.append(number)
        div_by_5 += 1


print(f'There is {div_by_4} numbers divided by 4: {div_by_4_numbers}')
print(f'There is {div_by_5} numbers divided by 4: {div_by_5_numbers}')
