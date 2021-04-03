word_a = input('Podaj pierwsze slowo: ').lower()
word_b = input('Podaj drugie slowo: ').lower()

different_chars = set(word_a) ^ set(word_b)

print(f'Znaki nie wspólne dla tych słow to: {different_chars}')


