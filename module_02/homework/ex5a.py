word1 = input('Podaj slowo: ')

word1 = ''.join(word1.split(' '))

if word1 == word1[::-1]:
    print('To jest palindrom')
else:
    print('To nie jest palindrom')