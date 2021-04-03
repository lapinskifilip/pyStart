pol_eng = {
    'dom': 'house',
    'kuchnia': 'kitchen',
    'ogrod': 'garden',
    'lazienka': 'bathroom'
}

word = input('Jakie slowo chcesz przetlumaczyc: ').lower()

for pl, eng in pol_eng.items():
        if word in pl:
            print(f'{pl} in english is {eng}')
            quit()
        if word in eng:
            print(f'{eng} po polsku to {pl}')
            quit()

print('Nie znam tego slowa')
