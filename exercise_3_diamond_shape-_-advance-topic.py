def print_diamond():
    while True:
        n = int(input('Enter odd integer: '))

        if n % 2 == 0:
            print('Please provide an odd integer.')
        else:
            break

        for i in range(n // 2 + 1):
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

        for i in range(n // 2 - 1, -1, -1):
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))


print_diamond()
