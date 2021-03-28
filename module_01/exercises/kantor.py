usd_buy = 3.8507
usd_sell = 3.9285

buy_or_sell = input('Witaj, chcesz kupic czy sprzedac? [Kupic/Sprzedac]: ').upper()

if buy_or_sell == 'KUPIC':
    currency = input(f'Chcesz {buy_or_sell} USD czy PLN?: ').upper()
    cash = int(input(f'Jaka kwote {currency} chcesz kupic?: '))
    if currency == 'USD':
        money = cash * usd_buy
        print(f'Aby kupic {cash} USD musisz zaplacic {int(money)} PLN')
    elif currency == 'PLN':
        money = cash / usd_sell
        print(f'Aby kupic {cash} PLN musisz zaplacic {int(money)} USD')
    else:
        print('Wystapil blad!')
elif buy_or_sell == 'SPRZEDAC':
    currency = input(f'Chcesz {buy_or_sell} USD czy PLN?: ').upper()
    cash = int(input(f'Jaka kwote {currency} chcesz sprzedac?: '))
    if currency == 'USD':
        money = cash * usd_buy
        print(f'Sprzedajac {cash} USD otrzymasz {int(money)} PLN')
    elif currency == 'PLN':
        money = cash / usd_buy
        print(f'Sprzedajac {cash} PLN otrzymasz {int(money)} USD')
    else:
        print('Wystapil blad!')
else:
    print('Wystapil blad!')
