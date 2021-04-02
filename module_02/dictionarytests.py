text = input('Podaj jakis tekst, a ja policze slowa: ')

text_list = text.split(" ")

counter = {}

for word in text_list:
    if word not in counter:
        counter[word] = 0
    counter[word] += 1

for x, y in counter.items():
    print(f'Slowo: "{x}" znajduje się w tekscie {y} razy.')
