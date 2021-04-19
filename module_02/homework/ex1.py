# counting char's from text.

text = input('Podaj jakis tekst, a ja podlicze znajdujace sie w nim znaki: ')

text_letters = {}

for char in text:
    if char not in text_letters:
        text_letters[char] = 0
    text_letters[char] += 1

for letter, count in text_letters.items():
    print(f'Znak {letter} znajduje sie w tym tekscie {count} razy')