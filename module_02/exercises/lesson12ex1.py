pol_en = {
    'dom': 'house',
    'kuchnia': 'kitchen',
    'ogrod': 'garden',
    'lazienka': 'bathroom'
}

en_pol = {}


for pl, en in pol_en.items():
    en_pol[en] = pl

pick = input('Jakiego slownika chcesz uzyc? \n [1. POL-EN / 2. EN-POL]: ')
if pick not in ['1', '2']:
    print('Error')
if pick == '1':
    word = input('Wybrales slownik POL-EN. Podaj polskie slowo: ').lower()
    if word not in pol_en:
        print('Nie ma takiego slowa w slowniku')
        quit()
    else:
        print(f'To slowo znaczy w jezyku Angielskim to: {pol_en[word]}')
else:
    word = input('Wybrales slownik EN-POL. Podaj angielskie slowo: ').lower()
    if word not in en_pol:
        print('Nie ma takiego slowa w slowniku')
        quit()
    else:
        print(f'To slowo znaczy w jezyku Angielskim to: {en_pol[word]}')

