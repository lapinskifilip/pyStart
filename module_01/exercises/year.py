name = input('Jak masz na imie?: ')
age = int(input('Podaj swoj wiek: '))
born = current_year - age
current_year = 2021

print(f'Witaj {name}, miło Cie poznać. Urodziłeś się w {born} roku.')
if current_year - born >= 18:
    print(f'{name}, widze ze jestes pelnoletni :)')
if born % 4 == 0 and born % 100 == 1 or born % 400 == 0:
    print(f'{name}, ale fajnie! Urodziles sie w roku przestepnym')


