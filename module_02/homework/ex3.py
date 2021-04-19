text = input('Podaj tekst do szyfrowania / odszyfrowania: ')
option = input('Chcesz zaszyfrowac [1], czy odszyfrowac [2] ?: ')

if option == '1':
    result = ''
    for char in text:
        if ord(char) >= ord('x'):
            result += chr(ord(char) - 23)
        else:
            result += chr(ord(char) + 3)

    print(result)

elif option == '2':
    result = ''
    for char in text:
        if ord(char) >= ord('d') or char == '#':
            result += chr(ord(char) - 3)
        else:
            result += chr(ord(char) + 23)

    print(result)
else:
    print('Nie rozumiem')