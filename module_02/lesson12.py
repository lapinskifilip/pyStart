products = {
    'Granaty' : 650,
    'Kalashnikov' : 13000,
    'Proch' : 15,
    'MP40' : 5400
}

for item, cost in products.items():
    print(f'{item} kosztuje {cost} PLN')

product = input('Co podac?: ')
price = products[product]

if product not in products:
    print('Nie mamy tego')

quantity = int(input('Podaj ilosc: '))
print(f'Do zaplaty: {quantity * price}')