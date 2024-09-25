def print_diamond():
    n = int(input('Enter odd integer: '))

    if n % 2 == 0:
        print('Please provide an odd integer.')

    else:
        for i in range(n // 2 + 1):
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

        
