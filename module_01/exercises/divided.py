number = int(input('Podaj liczbe calkowita: '))

number_list = [int(x) for x in str(number)]

unpair_numbers = number_list[::2]
pair_numbers = number_list[1::2]

sum = sum(unpair_numbers) - sum(pair_numbers)

div_by_5 = number_list[-1] == 5 or number_list[-1] == 0
div_by_11 = sum % 11 == 0

if div_by_5 and div_by_11:
    print('Podzielne przez 5 i przez 11')
elif div_by_5:
    print('Podzielne przez 5')
elif div_by_11:
    print('Podzielne przez 11')
else:
    print('Niepodzielne ani przez 5 ani przez 11')
