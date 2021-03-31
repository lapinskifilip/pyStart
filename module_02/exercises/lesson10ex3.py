number = int(input('Please give me a number: '))

if number <= 1:
    print(f'{number} is not a prime number')
else:
    if number == 2:
        print(f'{number} is a prime number')
        exit()
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            print(f'{number} is not a prime number')
            exit()
    print(f'{number} is a prime number')