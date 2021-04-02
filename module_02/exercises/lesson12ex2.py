big_text = input('Podaj mi jakis tekst: ')

word_count = {}

for word in big_text.lower().split():
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1
for one_word, count in word_count.items():
    print(f'Slowo: {one_word} znajduje się w tekscie {count} razy.')