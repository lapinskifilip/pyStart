eng_dictionary = {
    'dom': 'house',
    'kuchnia': 'kitchen',
    'ogrod': 'garden',
    'lazienka': 'bathroom'
}

translate = input('Na jaki jezyk chcesz przetlumaczyc? [PL/EN]: ').lower()
if translate != "pl" and translate != "en":
    print('Nie znam tego jezyka!')
    quit()
word = input('Jakie slowo chcesz przetlumaczyc: ').lower()
if word not in eng_dictionary:
    print('Nie mam takiego slowa w slowniku!')
    quit()

for pl, eng in eng_dictionary.items():
    if translate == "pl" and word in pl:
        print(f'{pl} po angielsku to {eng}')
        quit()
    if translate == "en" and word in eng:
        print(f'{eng} in polish is {pl}')
        quit()