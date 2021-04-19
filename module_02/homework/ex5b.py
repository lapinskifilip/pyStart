word1 = input('Podaj slowo 1: ')
word2 = input('Podaj slowo 2: ')

if sorted(word1) == sorted(word2):
    print('To są anagramy')
else:
    print('To nie są anagramy')